# src/api/app.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from pathlib import Path
import uuid
import soundfile as sf

app = FastAPI(title="Voice Auth API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path("data/processed")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@app.get("/")
def root():
    return {"status": "ok", "msg": "Voice Auth API running"}

@app.post("/upload_probe/")
async def upload_probe(file: UploadFile = File(...)):
    if not file.filename.endswith((".wav", ".flac")):
        raise HTTPException(status_code=400, detail="Only .wav/.flac supported")
    file_id = f"{uuid.uuid4().hex}.wav"
    out_path = UPLOAD_DIR / file_id
    content = await file.read()
    with open(out_path, "wb") as f:
        f.write(content)
    # for now return path; later pipeline will process it
    return {"filename": file_id, "path": str(out_path)}

if __name__ == "__main__":
    uvicorn.run("src.api.app:app", host="0.0.0.0", port=8000, reload=True)
