from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class AuthorSchema(BaseModel):
    id: UUID
    name: str
    user_id: Optional[UUID] = None  # nullable
    bio: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
