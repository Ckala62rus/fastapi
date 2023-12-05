from pydantic import BaseModel, EmailStr
from sqlalchemy import (
    Column,
    String,
    Integer,
    Text,
    DateTime,
    Boolean
)
from core.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, unique=True)
    date = Column(DateTime)
    email: EmailStr = Column("email", nullable=False, unique=True)
    password: str = Column("password", nullable=False)

    class ConfigDict:
        from_attributes = True


class UserLoginSchema(BaseModel):
    email: EmailStr = Column("email", nullable=False)
    password: str = Column("password", nullable=False)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "admin@main.ru",
                "password": "123123"
            }
        }
