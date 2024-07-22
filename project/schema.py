# from ninja import Schema
from typing import Optional, List
# from datetime import datetime  # Import datetime

from .models import Project
# from account.schema import UserSchemaOut

# from .models import Category

from ninja import ModelSchema
from django.core.validators import URLValidator

class ProjectSchema(ModelSchema):
    class Meta:
        model = Project
        fields = '__all__'  # Include all fields by default

    # Optional: Customize specific fields
    url: Optional[str] = None  # Use a plain string field for URL
    github: Optional[str] = None  # Use a plain string field for github

    def validate_url(self, value):
        if value and not URLValidator()(value):
            raise ValueError("Invalid URL format")

    def validate_github(self, value):
        if value and not URLValidator()(value):
            raise ValueError("Invalid Github URL format")