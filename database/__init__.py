from sqlalchemy.ext.asyncio import AsyncSession
# database/models/__init__.py
from database.models.user import User
from database.models.author import Author
from database.models.poem import Poem
from database.models.likes import Likes
from database.models.pond import Pond
from database.models.pondpoem import PondPoem
from database.setup import AsyncSessionLocal

async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session  # Auto-closes session after use
