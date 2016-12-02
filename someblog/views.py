from django.shortcuts import render


def index(request):
    return NotImplementedError()


def post(request, slug):
    return NotImplementedError()


def tag(request, slug):
    return NotImplementedError()
