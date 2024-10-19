from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.config.database import Session
from app.api.models.specialization import Specialization
from datetime import datetime

class SpecializationRequest(BaseModel):
    name: str
    description: str
    initialPrompt: str

router = APIRouter()

@router.post("/specialization")
async def create_specialization(request: SpecializationRequest):
    if not request.name:
        raise HTTPException(status_code=400, detail="Name cannot be empty")
    if not request.description:
        raise HTTPException(status_code=400, detail="Description cannot be empty")
    if not request.initialPrompt:
        raise HTTPException(status_code=400, detail="InitialPrompt cannot be empty")
    
    db = Session()
    new_specialization = Specialization(name=request.name, description=request.description, initialPrompt=request.initialPrompt, created_at=datetime.now(), updated_at=datetime.now())
    db.add(new_specialization)
    db.commit()
    return {"name": request.name, "description": request.description, "initialPrompt": request.initialPrompt}

@router.get("/specialization")
async def get_specializations():
    db = Session()
    specializations = db.query(Specialization).all()
    return specializations

@router.get("/specialization/{specialization_name}")
async def get_specialization(specialization_name: str):
    db = Session()
    specialization = db.query(Specialization).filter(Specialization.name == specialization_name).first()
    return specialization

@router.put("/specialization/{specialization_name}")
async def update_specialization(specialization_name: str, request: SpecializationRequest):
    db = Session()
    specialization = db.query(Specialization).filter(Specialization.name == specialization_name).first()
    specialization.name = request.name
    specialization.description = request.description
    specialization.initialPrompt = request.initialPrompt
    specialization.updated_at = datetime.now()
    db.commit()
    return {"name": request.name, "description": request.description, "initialPrompt": request.initialPrompt}

@router.delete("/specialization/{specialization_name}")
async def delete_specialization(specialization_name: str):
    db = Session()
    specialization = db.query(Specialization).filter(Specialization.name == specialization_name).first()
    db.delete(specialization)
    db.commit()
    return {"name": specialization_name, "status": "deleted"}




