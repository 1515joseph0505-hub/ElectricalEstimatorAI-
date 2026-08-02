from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

app = FastAPI(title="Electrical Estimator AI")

@app.get("/")
def home():
    return {
        "status": "running",
        "version": "1.0"
    }

@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    contents = await file.read()

    return JSONResponse(
        {
            "filename": file.filename,
            "size": len(contents),
            "message": "Drawing uploaded successfully.",
            "counts": {
                "lights": 0,
                "switches": 0,
                "sockets": 0,
                "dbs": 0
            }
        }
    )