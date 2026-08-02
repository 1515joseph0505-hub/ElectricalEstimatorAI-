from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Electrical Estimator AI API is running."
    }