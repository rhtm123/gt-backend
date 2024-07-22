
from ninja import Schema
from typing import Optional, List
from datetime import datetime  # Import datetime

from .models import Page
from account.schema import UserSchemaOut

from .models import Category

class CategorySchemaOut(Schema):
    id: int 
    name: str
    description: Optional[str] = None

    class Config:
        model = Category

# class TagSchema(Schema):
#     id: int  # Optional for output, required for update
#     name: str
#     description: str = None  # Optional field
#     popularity: int
#     slug: str = None  # Optional field (derived from name)

#     class Config:
#         model = Tag
#         # Include all fields by default
#         model_fields = '__all__'

class PageSchemaIn(Schema):
    id: int  # Optional for output, required for update
    title: str
    domain_name: str = None
    seo_title: str = None
    seo_description: str = None
    content: str
    is_published: bool
    img: Optional[str] = None  # URL path to the image
    # author: int  # Foreign key ID (consider using a separate UserSchema for detail)
    views: int
    read_time: int  # Minutes
    likes: int
    dislikes: int
    # tags: List[TagSchema] = []  # List of nested Tag schemas

    class Config:
        model = Page
        # model_fields = '__all__'  # Or explicitly list desired fields

class PageSchemaOut(Schema):
    id: int  # Optional for output, required for update
    title: str
    category: Optional[CategorySchemaOut] = None # Uncomment if you add a Category model
    domain_name: Optional[str] = None
    seo_title: str = None
    seo_description: str = None
    content: str
    slug: str = None  # Optional field (derived from title)
    is_published: bool
    img: Optional[str] = None  # URL path to the image
    author: UserSchemaOut  # Use the UserSchema for author details

    # author: int  # Foreign key ID (consider using a separate UserSchema for detail)
    views: int
    read_time: int  # Minutes
    likes: int
    dislikes: int
    # tags: List[TagSchema] = []  # List of nested Tag schemas
    created: datetime
    updated: datetime

    class Config:
        model = Page
        model_fields = '__all__'  # Or explicitly list desired fields