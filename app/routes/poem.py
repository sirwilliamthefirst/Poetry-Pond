import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database.models.poem import Poem
from database.schemas.poem import PoemSchema, CreatePoemSchema
from database import get_db

router = APIRouter(prefix="/poems", tags=["poems"])
@router.get("/", response_model=list[PoemSchema])
async def get_poems(user_id: uuid.UUID = None, limit: int = 10, db: AsyncSession = Depends(get_db)):
    query = select(Poem)
    if user_id:
        query = query.where(Poem.user_id == user_id)
    query = query.limit(limit)
    result = await db.execute(query)
    poems = result.scalars().all()
    return poems


@router.get("/{poem_id}", response_model=PoemSchema)
async def get_poem(poem_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Poem).where(Poem.id == poem_id))
    poem = result.scalars().first()
    if not poem:
        raise HTTPException(status_code=404, detail="Poem not found")
    return poem

@router.post("/", response_model=PoemSchema, status_code=201)
async def add_poem(poemData: CreatePoemSchema, db: AsyncSession = Depends(get_db)):
    poem = Poem(**poemData.model_dump())
    db.add(poem)
    await db.commit()
    await db.refresh(poem)
    return poem