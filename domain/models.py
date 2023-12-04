from core.db import Base
from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from user.user import User


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    title = Column(String)
    text = Column(Text)
    date = Column(DateTime)
    user = Column(Integer, ForeignKey("users.id"))
    user_id = relationship(User)
