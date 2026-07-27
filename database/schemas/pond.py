from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class PondSchema(BaseModel):
    id: UUID
    user_id: UUID
    name: str
    description: Optional[str] = None
    is_public: bool
    is_default: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class PondPoemSchema(BaseModel):
    pond_id: UUID
    poem_id: UUID
    added_at: datetime

    class Config:
        from_attributes = True