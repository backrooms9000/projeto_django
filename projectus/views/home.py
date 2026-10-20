from django.shortcuts import render
from django.conf import settings


def home(request):

    posts = post.objects.all()
    context = {
        'tag_title': f'{settings.SITENAME}',
        'posts': posts
    }

    return render(
        request,
        'projectus/home.html',
        context
    )
