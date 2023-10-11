import logging
import os
from datetime import datetime

import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

from src.client.Minio import put_in_minio, MINIO_URL

# from src.service.stable_diffusion_service import draw_with_prompt
# from src.service.stable_diffusion_xl.stable_diffusion_xl import draw_with_prompt_in_xl

logger = logging.getLogger()

# get current working directory
current_directory = os.getcwd()
logger.info(f"Current directory: {current_directory}")

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wellcome to the Generate Server"}


# Health Check
@app.get("/health_check")
async def health_check():
    return {"message": "OK"}


# POST health check
@app.post("/health_check")
async def health_check(body=None):
    return {"message": "OK", "body": body}


class DrawRequest(BaseModel):
    prompt: str = None
    negative_prompt: str = None
    openPrefix: bool = False


# draw an image
@app.post("/draw")
async def draw(body: DrawRequest = None):
    logger.info(f"""[/draw] prompt: {body.prompt}, negative_prompt: {body.negative_prompt}""")
    # image_path = draw_with_prompt(body.prompt, body.negative_prompt)
    # image_path = draw_with_prompt_in_xl(body.prompt, body.negative_prompt, body.openPrefix)

    image_names = [
        'image.jpg',
        'image2.jpg',
        'image.jpg',
        'image2.jpg',
    ]

    result_paths = []

    # 上传图片到minio
    time_string = datetime.now().isoformat()
    for i in range(0, len(image_names)):
        image = image_names[i]
        image_path = f"src/service/result/{image}"
        # add timestamp to image name
        image_object_name = f"{time_string}_{i + 1}_{image}"
        result = put_in_minio(image_object_name, image_path)
        logger.info(f"[draw] Saved image to {result}")
        result_paths.append('http://' + MINIO_URL + result)

    logger.info(f"[draw] Done drawing.")
    return {
        "images": result_paths,
        "used_time": 300000,
    }


log_config = uvicorn.config.LOGGING_CONFIG
# log
log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
log_config["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"

uvicorn.run(app, host="127.0.0.1", port=10102, log_config=log_config)
