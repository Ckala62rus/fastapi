from sqlalchemy import Column, Integer, String, Text

from core.db import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    title = Column(String)
    description = Column(Text)
