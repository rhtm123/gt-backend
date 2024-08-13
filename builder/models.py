from django.db import models
from imagekit.models import ProcessedImageField # type: ignore
from django.conf import settings

from django.template.defaultfilters import slugify


# This is project created by user
class Project(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,null=True, blank=True)

    jsondom = models.TextField()

    is_published = models.BooleanField(default=False)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="project_creator")
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

### This is pre-save json format
class Builder(models.Model):
    name = models.CharField(max_length=255)
    jsondom = models.TextField()

    img = ProcessedImageField(upload_to='gt/builder/', format='JPEG',options={'quality': 60 }, null=True,  blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    is_published = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name