from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from detector import analyze_pdf

app = FastAPI(title="Electrical Estimator AI")

@app.get("/")
def home():
    return {
        "status": "running",
        "version": "2.0"
    }

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    pdf = await file.read()

    result = analyze_pdf(pdf)

    return JSONResponse(content=result)