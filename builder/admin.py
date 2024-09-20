from django.contrib import admin

# Register your models here.

from .models import Builder, Project, ClassAllValues


class BuilderAdmin(admin.ModelAdmin):

    def creator_(self, obj):
        return obj.creator.username
    list_display = ("name", "creator_", "created")
    list_filter = ("creator",)


admin.site.register(Builder, BuilderAdmin)


class ProjectAdmin(admin.ModelAdmin):

    def creator_(self, obj):
        return obj.creator.username
    list_display = ("name", "creator_", "created")
    list_filter = ("creator",)


admin.site.register(Project, ProjectAdmin)



admin.site.register(ClassAllValues)