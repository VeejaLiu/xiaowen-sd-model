import logging

import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import FileResponse

from src.service.stable_diffusion_service import draw_with_prompt

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
    prompt: str


# draw an image
@app.post("/draw")
async def draw(body: DrawRequest = None):
    logging.info(f"""[/draw]""")
    image_path = draw_with_prompt(body.prompt)
    # image_path = 'src/service/result/image.jpg'
    return FileResponse(image_path)


uvicorn.run(app, host="127.0.0.1", port=10102)
