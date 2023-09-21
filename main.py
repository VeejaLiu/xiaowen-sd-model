from fastapi import FastAPI
from pydantic import BaseModel
from uvicorn import logging

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wellcome to the Generate Server"}


# Health Check
@app.get("/health_check")
async def health_get():
    return {"message": "OK"}


# POST health check, Get the body
@app.post("/health_check")
async def health_post(body=None):
    return {"message": f"OK {body}"}


class DrawRequest(BaseModel):
    prompt: str


# draw an image
@app.post("/draw")
async def draw(body: DrawRequest = None):
    print(f"""[/draw] {body}""")
    return {"message": f"OK {body}"}
