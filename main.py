import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import FileResponse

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
    some_file_path = "Cat.jpg"
    return FileResponse(some_file_path)

uvicorn.run(app, host="127.0.0.1", port=10102)
