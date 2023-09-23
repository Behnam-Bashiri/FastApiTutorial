from re import U
from tkinter import N
from typing import Union
from pydantic import BaseModel, EmailStr
from fastapi import FastAPI,Query,Form,File,UploadFile

app = FastAPI()

@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
