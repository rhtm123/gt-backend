from tag.models import Tag
from rest_framework import serializers

from typing import Dict, Any



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"