from typing import Optional
from pydantic import BaseModel, ConfigDict


class TaskSchema(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        from_attributes = True


class TaskSchemaAdd(BaseModel):
    title: str
    description: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Some name",
                    "description": "Lorem ipsum dollar sit amet",
                }
            ]
        }
    }


class TaskSchemaEdit(BaseModel):
    title: str
    description: str
