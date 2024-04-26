from model import model_pipeline
from typing import Union

from fastapi import FastAPI, UploadFile
from PIL import Image
import io

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome!"}


@app.post("/ask")
def ask(text: str, image: UploadFile):
    content = image.file.read()

    image = Image.open(io.BytesIO(content))

    result = model_pipeline(text, image)

    return {"answer": result}

