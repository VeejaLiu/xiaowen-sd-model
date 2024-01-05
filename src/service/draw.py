import base64
import io
from datetime import datetime
from PIL import Image

import requests

from env_config import SD_API_CONFIG
from src.client.Minio import put_in_minio_by_file_path, MINIO_URL, put_in_minio_by_file_object
from src.constant.TattooStyles import TattooStyles
from src.lib.logger import logger
from src.service.prompt import handle_prompt


def create_thumbnail(image_data, original_size=(512, 512), thumbnail_max_size=128):
    """
    创建并返回一个缩略图的BytesIO对象
    :param image_data: 原图的BytesIO对象
    :param original_size: 原图的尺寸, 默认为512x512
    :param thumbnail_max_size: 缩略图的最大边尺寸, 默认为128，即最大边为128
    """
    # 读取原图
    image = Image.open(image_data)
    # 计算缩略图的尺寸
    thumbnail_size = (thumbnail_max_size, thumbnail_max_size)
    if image.size[0] > image.size[1]:
        thumbnail_size = (thumbnail_max_size, int(thumbnail_max_size * image.size[1] / image.size[0]))
    else:
        thumbnail_size = (int(thumbnail_max_size * image.size[0] / image.size[1]), thumbnail_max_size)
    # 生成缩略图
    image.thumbnail(thumbnail_size)
    # 生成缩略图的BytesIO对象
    thumbnail_data = io.BytesIO()
    image.save(thumbnail_data, format='PNG')
    thumbnail_data.seek(0)
    return thumbnail_data


async def draw_with_prompt(prompt: str, style: TattooStyles):
    # If style is not specified, use default style
    if style is None or style not in TattooStyles:
        logger.info(f"[draw_with_prompt] Using default style: {TattooStyles.DOT_WORK}")
        style = TattooStyles.DOT_WORK
    logger.info(f"[draw_with_prompt] Drawing with prompt: {prompt}, style: {style}")

    # handle prompt
    style_config = handle_prompt(style, prompt)

    prompt = style_config['prompt']
    negative_prompt = style_config['negative_prompt']
    height = style_config['height']
    width = style_config['width']
    logger.info(
        f"[draw_with_prompt] Final prompt: {prompt}, negative_prompt: {negative_prompt}, height: {height}, width: {width}")

    url = SD_API_CONFIG['URL']
    headers = {"content-type": "application/json"}
    # {
    #   "prompt": "",
    #   "negative_prompt": "",
    #   "styles": [
    #     "string"
    #   ],
    #   "seed": -1,
    #   "subseed": -1,
    #   "subseed_strength": 0,
    #   "seed_resize_from_h": -1,
    #   "seed_resize_from_w": -1,
    #   "sampler_name": "string",
    #   "batch_size": 1,
    #   "n_iter": 1,
    #   "steps": 50,
    #   "cfg_scale": 7,
    #   "width": 512,
    #   "height": 512,
    #   "restore_faces": true,
    #   "tiling": true,
    #   "do_not_save_samples": false,
    #   "do_not_save_grid": false,
    #   "eta": 0,
    #   "denoising_strength": 0,
    #   "s_min_uncond": 0,
    #   "s_churn": 0,
    #   "s_tmax": 0,
    #   "s_tmin": 0,
    #   "s_noise": 0,
    #   "override_settings": {},
    #   "override_settings_restore_afterwards": true,
    #   "refiner_checkpoint": "string",
    #   "refiner_switch_at": 0,
    #   "disable_extra_networks": false,
    #   "comments": {},
    #   "enable_hr": false,
    #   "firstphase_width": 0,
    #   "firstphase_height": 0,
    #   "hr_scale": 2,
    #   "hr_upscaler": "string",
    #   "hr_second_pass_steps": 0,
    #   "hr_resize_x": 0,
    #   "hr_resize_y": 0,
    #   "hr_checkpoint_name": "string",
    #   "hr_sampler_name": "string",
    #   "hr_prompt": "",
    #   "hr_negative_prompt": "",
    #   "sampler_index": "Euler",
    #   "script_name": "string",
    #   "script_args": [],
    #   "send_images": true,
    #   "save_images": false,
    #   "alwayson_scripts": {}
    # }
    payload = {
        'prompt': prompt,
        'negative_prompt': negative_prompt,
        'batch_size': 4,
        'cfg_scale': 7,
        'steps': 28,
        "width": width,
        "height": height,

    }
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()
    result = response.json()

    images_data = result['images']

    # 上传图片到minio
    time_string = datetime.now().isoformat()
    result_paths = []
    # for image_base64 in images_data:
    for i in range(len(images_data)):
        image_data = base64.b64decode(images_data[i])
        image_data_io = io.BytesIO(image_data)

        # 生成缩略图
        thumbnail_data = create_thumbnail(image_data_io, original_size=(width, height), thumbnail_max_size=128)

        # 上传原图
        image_object_name = f"{time_string}_{i + 1}.png"
        original_result = put_in_minio_by_file_object(image_object_name, image_data)
        logger.info(f"[draw_with_prompt] Saved image to {result}")

        # 上传缩略图
        thumbnail_object_name = f"{time_string}_{i + 1}_thumbnail.png"
        thumbnail_result = put_in_minio_by_file_object(thumbnail_object_name, thumbnail_data)
        logger.info(f"[draw_with_prompt] Saved thumbnail to {result}")

        result_paths.append({
            'original': original_result,
            'thumbnail': thumbnail_result
        })

    logger.info(f"[draw_with_prompt] Done drawing.")
    return result_paths
