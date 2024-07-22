from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify

class Tag(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(null=True, blank=True)
	popularity = models.IntegerField(default=0)
	slug = models.SlugField(max_length=255, null=True, blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Tag, self).save(*args, **kwargs)

	def __str__(self):
		return self.name