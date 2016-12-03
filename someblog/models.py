from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.html import format_html

class Tag(models.Model):
    """A tag that describes many posts."""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        """Return tag name."""
        return self.name


class Author(models.Model):
    """Post author, contains bio and other information."""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bio = models.TextField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        """Return author name."""
        return self.name

    def get_absolute_url(self):
        """Get URL to author page."""
        return reverse('someblog.author', args=[self.slug])

    def link(self):
        """Return link to author page."""
        return format_html('<a href="{}">{}</a>', self.get_absolute_url(), self.name)



class Post(models.Model):
    """A blog post."""
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    tags = models.ManyToManyField(Tag)
    text = models.TextField()

    def __str__(self):
        """Return post title."""
        return self.title

    def get_absolute_url(self):
        """Get the absolute URL for this post."""
        return reverse('someblog.post', args=[self.slug])

    def title_link(self):
        """Return link to the post."""
        return format_html('<a href="{}">{}</a>', self.get_absolute_url(), self.title)

    def author_link(self):
        """Return link to the author page."""
        return self.author.link()
