from django.contrib import admin

# Register your models here.

from .models import Builder, Project

admin.site.register(Builder)

admin.site.register(Project)