from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class PondPoemSchema(BaseModel):
    pond_id: UUID
    poem_id: UUID
    added_at: datetime

    class Config:
        from_attributes = True