from fastapi import APIRouter, Depends, HTTPException, status # import from fastapi, not http.client
from app.auth.security import hash_password, verify_password
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database.models.user import User
from database.schemas.user import TokenResponse, UserLogin, UserSchema, UserCreate
from database import get_db
from app.auth.jwt import create_access_token, create_refresh_token
router = APIRouter(prefix="/user", tags=["users"])


@router.get("/", response_model=list[UserSchema])
async def get_users(email: str = None, db: AsyncSession = Depends(get_db)):
    query = select(User)
    if email:
        query = query.where(User.email == email)
    result = await db.execute(query)
    users = result.scalars().all()
    return users

@router.post("/register", response_model=UserSchema)
async def register(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    hashed = hash_password(user_in.password)
    user = user = User(email=user_in.email, username=user_in.username, password_hash=hashed)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

@router.post("/login", response_model=TokenResponse)
async def login(credentials: UserLogin, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == credentials.email))
    user = result.scalar_one_or_none()

    if not user or not verify_password(credentials.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    access_token = create_access_token({"sub": str(user.id)})
    refresh_token = create_refresh_token({"sub": str(user.id)})

    return TokenResponse(access_token=access_token, refresh_token=refresh_token)