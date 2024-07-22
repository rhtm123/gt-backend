from django.contrib import admin

# Register your models here.

from .models import Page, Category

admin.site.register(Category)
admin.site.register(Page)