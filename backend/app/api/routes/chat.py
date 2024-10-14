from fastapi import APIRouter, HTTPException
from app.core.mistral_service import get_chat_response
from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    
    
router = APIRouter()

@router.post("/chat")
async def chat_with_mistral(request: ChatRequest):
    if not request.message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    user_message = request.message
    response = get_chat_response(user_message)
    return {"response": response}
