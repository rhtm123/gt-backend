
from ninja import Schema
from typing import Optional, List
from datetime import datetime  # Import datetime

from .models import Builder, Project
from account.schema import UserSchemaOut


class ProjectSchemaOut(Schema):
    id: int  # Optional for output, required for update
    name: str
    jsondom: str = None
    slug: str = None  # Optional field (derived from title)
    is_published: bool

    creator: UserSchemaOut  # Use the UserSchema for author details

    created: datetime
    updated: datetime

    class Config:
        model = Project

class BuilderSchemaOut(Schema):
    id: int  # Optional for output, required for update
    name: str

    jsondom: str = None

    # slug: str = None  # Optional field (derived from title)
    is_published: bool
    img: Optional[str] = None  # URL path to the image
    creator: UserSchemaOut  # Use the UserSchema for author details

    # author: int  # Foreign key ID (consider using a separate UserSchema for detail)
    views: int

    created: datetime
    updated: datetime

    class Config:
        model = Builder
        # model_fields = '__all__'  # Or explicitly list desired fields