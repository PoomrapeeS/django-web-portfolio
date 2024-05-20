from django.db import models
from taggit.managers import TaggableManager


# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=500)
    published = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title
