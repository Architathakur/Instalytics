import asyncio
from app.database import engine
from app.models import models

async def init():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

asyncio.run(init())