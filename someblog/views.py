from django.shortcuts import render, get_object_or_404
from someblog.models import Post


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'Blog',
    }
    return render(request, "someblog/index.html", context)


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
        'title': post.title,
    }
    return render(request, "someblog/post.html", context)


def tag(request, slug):
    return NotImplementedError()


def author(request, slug):
    return NotImplementedError()


def tags(request, slug):
    return NotImplementedError()


def authors(request, slug):
    return NotImplementedError()
