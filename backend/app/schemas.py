from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import time, date

class SubscribeRequest(BaseModel):
    email: EmailStr
    project: str
    location: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None