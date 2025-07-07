import random
from datetime import datetime, timedelta

async def get_profile_data(username: str):
    # This is a mock function - replace with real Instagram API integration later
    return {
        "username": username,
        "full_name": f"{username.capitalize()} User",
        "followers_count": random.randint(1000, 100000),
        "following_count": random.randint(100, 1000),
        "posts_count": random.randint(10, 500),
        "engagement_rate": round(random.uniform(1.0, 10.0), 2),
        "bio": "✨ Digital Creator | Living my best life",
        "profile_pic_url": f"https://api.dicebear.com/7.x/avataaars/svg?seed={username}",
        "is_verified": random.choice([True, False]),
        "last_updated": datetime.utcnow()
    }

async def get_mock_analytics(username: str):
    return {
        "profile_username": username,
        "date": datetime.utcnow(),
        "likes": random.randint(100, 1000),
        "comments": random.randint(10, 100),
        "engagement_rate": round(random.uniform(1.0, 10.0), 2),
        "followers": random.randint(1000, 100000)
    }