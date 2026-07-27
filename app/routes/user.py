from fastapi import APIRouter, Depends, HTTPException  # import from fastapi, not http.client

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database.models.user import User
from database.schemas.user import UserSchema
from database import get_db

router = APIRouter(prefix="/user", tags=["users"])


@router.get("/", response_model=list[UserSchema])
async def get_users(email: str = None, db: AsyncSession = Depends(get_db)):
    query = select(User)
    if email:
        query = query.where(User.email == email)
    result = await db.execute(query)
    users = result.scalars().all()
    return users


#@router.post("/login")
#async def login(credentials: LoginSchema, db: AsyncSession = Depends(get_db)):
 #   query = select(User).where(User.email == credentials.email)
  #  result = await db.execute(query)
   # user = result.scalar_one_or_none()
    #if not user:
     #   raise HTTPException(status_code=404, detail="User not found")
    # verify password here
    #return user