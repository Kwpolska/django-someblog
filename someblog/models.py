from django.conf import settings
from django.db import models

class Tag(models.Model):
    name = models.TextField(max_length=100)
    slug = models.SlugField(max_length=100)


class Author(models.Model):
    name = models.TextField(max_length=100)
    slug = models.SlugField(max_length=100)
    bio = models.TextField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Post(models.Model):
    title = models.TextField(max_length=100)
    slug = models.SlugField(max_length=100)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
