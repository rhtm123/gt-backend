from django.shortcuts import render

# Create your views here.

from tag.models import Tag 
from tag.serializers import TagSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class TagListCreate(generics.ListCreateAPIView):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)
	filter_backends = (DjangoFilterBackend, filters.SearchFilter)
	search_fields = ('name', 'description')
	pagination_class = PageNumberPagination

class TagGetUpdate(generics.RetrieveUpdateAPIView):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer
	permission_classes = (AllowAny,)

class TagGetUpdateSlug(generics.RetrieveUpdateAPIView):
	query_pk_and_slug = True
	queryset = Tag.objects.all()
	serializer_class = TagSerializer
	permission_classes = (AllowAny,)

class TagDelete(generics.DestroyAPIView):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)