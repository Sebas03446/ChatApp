from app.core.config.database import Base
from sqlalchemy import Column, Integer, String, DateTime

class Specialization(Base):
    __tablename__ = "specializations"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,index=True, unique=True)
    description = Column(String, index=True)
    initialPrompt = Column(String, index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)