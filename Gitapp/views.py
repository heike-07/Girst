from django.shortcuts import render
from django.http import HttpResponse

from . import models


# Create your views here.

def index(request):
    articles = models.Article.objects.all()
    return render(request, 'Gitapp/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'Gitapp/page.html', {'article': article})
