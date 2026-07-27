from sqlalchemy import Column, Text, Boolean, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, DeclarativeBase
from sqlalchemy.sql import func
from database.setup import Base

class PondPoem(Base):
    __tablename__ = "pond_poems"

    pond_id = Column(UUID(as_uuid=True), ForeignKey("ponds.id"), primary_key=True)
    poem_id = Column(UUID(as_uuid=True), ForeignKey("poems.id"), primary_key=True)
    added_at = Column(DateTime(timezone=True), server_default=func.now())

    pond = relationship("Pond", back_populates="pond_poems")
    poem = relationship("Poem", back_populates="pond_poems")