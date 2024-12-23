from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from typing import List, Union

class Settings(BaseSettings):
    PROJECT_NAME: str = "My ChatAPP FastAPI Project"
    API_V1_STR: str = "/api/v1"
    SENTRY_DSN: Union[str, None] = None
    ENVIRONMENT: str = "local"  
    CORS_ORIGINS: List[str] = ["http://localhost:8080"]  

    model_config = ConfigDict(env_file=".env") 

settings = Settings()
