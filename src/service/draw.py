import base64
import io
from datetime import datetime

import requests

from env_config import SD_API_CONFIG
from src.client.Minio import put_in_minio_by_file_path, MINIO_URL, put_in_minio_by_file_object
from src.constant.TattooStyles import TattooStyles
from src.lib.logger import logger
from src.service.prompt import handle_prompt


async def draw_with_prompt(prompt: str, style: TattooStyles):
    # If style is not specified, use default style
    if style is None or style not in TattooStyles:
        logger.info(f"[draw_with_prompt] Using default style: {TattooStyles.BLACK_WORK}")
        style = TattooStyles.BLACK_WORK
    logger.info(f"[draw_with_prompt] Drawing with prompt: {prompt}, style: {style}")

    # handle prompt
    new_prompt = handle_prompt(style, prompt)
    negative_prompt = (f"nsfw, worst quality, low quality, normal quality, lowresolution, low resolution, "
                       f"poor anatomical structure, poor hand, text, errors, missing fingers, multiple fingers, "
                       f"few fingers, cropped, worst quality, low quality, normal quality, jpeg artifacts, "
                       f"signature, watermark, username, blurry, exposed, nipple, penis, penis, vagina, anus, "
                       f"underwear,Breast cleavage, sexy clothing,Not wearing clothes, boobs, Naked chest,"
                       f"nipple protrusion,expose the body")
    logger.info(f"[draw_with_prompt] Final prompt: {new_prompt}")

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
        'prompt': new_prompt,
        'negative_prompt': negative_prompt,
        'batch_size': 4,
        'cfg_scale': 7.5,
        'steps': 30,
        "width": 768,
        "height": 768,

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
        image_data = io.BytesIO(image_data)
        image_object_name = f"{time_string}_{i + 1}.png"
        result = put_in_minio_by_file_object(image_object_name, image_data)
        logger.info(f"[draw_with_prompt] Saved image to {result}")
        result_paths.append('http://' + MINIO_URL + result)

    logger.info(f"[draw_with_prompt] Done drawing.")
    return result_paths
