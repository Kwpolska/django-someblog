from django.contrib import admin
from someblog.models import Post, Tag, Author

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Author)
