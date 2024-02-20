from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app: FastAPI = FastAPI()
port = getenv("PORT")

@app.get("/")
async def health_check():
    return {
        "success": True,
        "message": "Hello from SMS spam classifier API",
        "code": 200
    }

uvicorn.run(app, port=int(port))
