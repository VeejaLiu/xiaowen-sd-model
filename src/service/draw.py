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
    logger.info(f"[draw_with_prompt] Final prompt: {new_prompt}")

    url = SD_API_CONFIG['URL']
    headers = {"content-type": "application/json"}
    payload = {'prompt': new_prompt}
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
