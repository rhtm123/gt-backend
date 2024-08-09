# from ninja import Schema
from typing import Optional, List
# from datetime import datetime  # Import datetime

from .models import Project
# from account.schema import UserSchemaOut

# from .models import Category
from ninja import ModelSchema, Schema
from django.core.validators import URLValidator

# Define a schema for the User model
class UserSchema(Schema):
    id: int
    username: str
    email: Optional[str] = None

# Define a schema for the Technology model
class TechnologySchema(Schema):
    id: int
    name: str
    icon: Optional[str] = None

class ProjectSchema(ModelSchema):
    
    
    class Meta:
        model = Project
        fields = '__all__'  # Include all fields by default
        # depth = 3

    # Optional: Customize specific fields
    url: Optional[str] = None  # Use a plain string field for URL
    github: Optional[str] = None  # Use a plain string field for github

    def validate_url(self, value):
        if value and not URLValidator()(value):
            raise ValueError("Invalid URL format")

    def validate_github(self, value):
        if value and not URLValidator()(value):
            raise ValueError("Invalid Github URL format")
        
    client: UserSchema  # Use the UserSchema for the client field
    technology_used: List[TechnologySchema]