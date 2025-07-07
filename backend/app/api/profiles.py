from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from .. import models
from ..utils.instagram import get_profile_data
from typing import Optional
from sqlalchemy import select
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/{username}")
async def get_profile(
    username: str,
    db: AsyncSession = Depends(get_db)
):
    # Check if we have recent profile data in database
    async with db as session:
        query = select(models.Profile).where(
            models.Profile.username == username,
            models.Profile.last_updated >= datetime.utcnow() - timedelta(hours=24)
        )
        result = await session.execute(query)
        profile = result.scalar_one_or_none()

        if profile:
            return profile

        # If no recent data, fetch from Instagram
        try:
            profile_data = await get_profile_data(username)
            new_profile = models.Profile(**profile_data)
            session.add(new_profile)
            await session.commit()
            return new_profile
        except Exception as e:
            raise HTTPException(status_code=404, detail=str(e))