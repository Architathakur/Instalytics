from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from ..database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    favorites = relationship("Favorite", back_populates="user")

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String)
    followers_count = Column(Integer)
    following_count = Column(Integer)
    posts_count = Column(Integer)
    engagement_rate = Column(Float)
    bio = Column(String)
    profile_pic_url = Column(String)
    is_verified = Column(Boolean, default=False)
    last_updated = Column(DateTime, default=datetime.utcnow)

class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    profile_username = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="favorites")

class Analytics(Base):
    __tablename__ = "analytics"

    id = Column(Integer, primary_key=True, index=True)
    profile_username = Column(String, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    likes = Column(Integer)
    comments = Column(Integer)
    engagement_rate = Column(Float)
    followers = Column(Integer)