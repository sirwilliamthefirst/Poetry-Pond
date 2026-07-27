from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class PoemSchema(BaseModel):
    id: UUID
    user_id: UUID
    title: str
    author: str
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CreatePoemSchema(BaseModel):
    user_id: UUID
    title: str
    author: str
    content: str

    class Config:
        from_attributes = True
