from django.db import models
from django.conf import settings
# from tag.models import Tag
from django.template.defaultfilters import slugify

from imagekit.models import ProcessedImageField # type: ignore
from imagekit.processors import ResizeToFill # type: ignore

from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify


from django.db import models

from django.template.defaultfilters import slugify


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255,null=True, blank=True)

    description = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)



# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    domain_name = models.CharField(max_length=255, blank=True, null=True,)
    seo_title = models.TextField(null=True, blank=True, max_length=100)
    seo_description = models.TextField(null=True, blank=True, max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255,null=True, blank=True)
    is_published = models.BooleanField(default=False)

    img = ProcessedImageField(upload_to='gt/blog/', processors=[ResizeToFill(1280, 720)], format='JPEG',options={'quality': 60 }, null=True,  blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    
    views = models.IntegerField(default=0)
    read_time = models.IntegerField(default=0) # in minutes
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    # tags = models.ManyToManyField(Tag, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)


    def __str__(self):
        return self.title