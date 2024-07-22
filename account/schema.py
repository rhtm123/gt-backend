from django.contrib.auth.models import User

from ninja import Schema
from typing import Optional, List
from datetime import datetime  # Import datetime

class UserSchemaOut(Schema):
    id: int  # User ID (primary key)
    username: str
    first_name: str = None  # Optional field
    last_name: str = None  # Optional field
    email: str = None  # Optional field, depending on your needs
    is_superuser: bool = False  # Indicates superuser status

    class Config:
        # Explicitly define schema fields to avoid exposing sensitive data
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_superuser'] 