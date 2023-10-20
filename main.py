import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from src.lib.logger import logger
from src.service.draw import draw_with_prompt, TattooStyles

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


class DrawRequest(BaseModel):
    prompt: str = None
    style: TattooStyles = 0


# draw an image
@app.post("/draw")
async def draw(body: DrawRequest = None):
    logger.info(f"""[/draw] prompt: {body.prompt}, style: {body.style}""")
    result = await draw_with_prompt(body.prompt, body.style)
    return result

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=10102)
