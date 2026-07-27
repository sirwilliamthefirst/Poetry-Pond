from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class UserSchema(BaseModel):
    id: UUID
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True