from fastapi import FastAPI, Response
import uvicorn
from dotenv import load_dotenv
from os import getenv
from pydantic import BaseModel, ValidationError
from services.get_text_spm_prediction import get_text_spam_prediction

load_dotenv()

app: FastAPI = FastAPI()
port = getenv("PORT")
env = getenv("ENV")

# TODO: Can be refactored but let's do we need router isolation or not. 
class CheckReqBody(BaseModel):
    message: str

@app.get("/")
async def health_check():
    return {
        "success": True,
        "message": "Hello from SMS spam classifier API",
        "code": 200
    }
    
@app.post("/check-message-quality")
async def check_message_quality(req_body: CheckReqBody, response: Response):
    try:
        sms = req_body.message
        result = get_text_spam_prediction(str(sms))
        
        isSpam = False
        
        if result == 1:
            isSpam = True
        
        response.status_code = 200
        return {
            "success": True,
            "code": 200,
            "data": {
                "isSpam": isSpam
            }
        }
    except ValidationError:
        response.status_code = 400
        
        return {
            "code": 400,
            "success": False,
            "error": ValidationError.errors[0]
        }   
    except:
        response.status_code = 500
        
        return {
            "code": 500,
            "success": False,
            "error": "Internal Server Error!!"
        }

uvicorn.run(app, host="0.0.0.0", port=int(port))
