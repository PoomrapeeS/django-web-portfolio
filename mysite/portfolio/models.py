from django.db import models
from taggit.managers import TaggableManager


# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    description = models.TextField()
    technologies = models.TextField()  # Store as text separated by commas
    resources = models.TextField()  # Store as text separated by commas
    images = models.TextField()  # Store as text separated by commas
    published = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title
