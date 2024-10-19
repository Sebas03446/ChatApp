from fastapi import APIRouter, HTTPException
from app.core.mistral_service import get_chat_response
from pydantic import BaseModel
from app.api.models.specialization import Specialization
from app.core.config.database import Session


class ChatRequest(BaseModel):
    message: str
    specialization: str = None
    
    
router = APIRouter()

@router.post("/chat")
async def chat_with_mistral(request: ChatRequest):
    if not request.message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    if request.specialization:
        db = Session()
        specialization = db.query(Specialization).filter(Specialization.name == request.specialization).first()

        if not specialization:
            raise HTTPException(status_code=404, detail="Specialization not found")
        
        response = get_chat_response(request.message, specialization.initialPrompt)
        return {"message": request.message, "specialization": request.specialization, "response": response}
    
    user_message = request.message
    response = get_chat_response(user_message)
    return {"response": response}
