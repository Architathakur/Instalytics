from fastapi import APIRouter, HTTPException, Depends
from ..utils.analytics import calculate_analytics
from ..models.analytics import AnalyticsResponse
from typing import List
from ..utils.auth import get_current_user

router = APIRouter()

@router.get("/{username}", response_model=AnalyticsResponse)
async def get_analytics(
    username: str,
    current_user: dict = Depends(get_current_user)
):
    try:
        analytics_data = await calculate_analytics(username)
        return analytics_data
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/compare", response_model=List[AnalyticsResponse])
async def compare_profiles(
    usernames: List[str],
    current_user: dict = Depends(get_current_user)
):
    try:
        comparisons = [await calculate_analytics(username) for username in usernames]
        return comparisons
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))