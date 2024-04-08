import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator

from Tengri.models import Article
from Tengri.utils.get_authors import ArticleAuthors
from Tengri.utils.get_tags import ArticleParser


# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-project_date')
    paginator = Paginator(articles, 15)
    page = request.GET.get('page')
    news = paginator.get_page(page)
    return render(request, 'index.html', {'articles': articles, 'news': news, 'tags': ArticleParser().get_tags()})


def search_articles(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        filters = request.POST.getlist('filtered')
        if len(filters) >= 1 and searched is not None:
            articles = Article.objects.filter(title__icontains=searched, project_tags__icontains=filters[0])
        elif searched is not None:
            articles = Article.objects.filter(title__icontains=searched)
        elif len(filters) >= 1:
            articles = Article.objects.filter(project_tags__icontains=filters)
        else:
            articles = Article.objects.all()
        return render(request, 'search_articles.html', {'filtered': filters, 'searched': searched, 'articles': articles})
    else:
        return render(request, 'search_articles.html', {})


def sorted_articles(request):
    order = request.POST.get('sorting')
    articles = Article.objects.all().order_by(order)
    return render(request, 'sorted_articles.html', {'news': articles, 'order': order})


def news(request, pk):
    article = Article.objects.get(project_id=f"{pk}")
    authors_list = ArticleAuthors().get_authors(f"{pk}")
    return render(request, 'news.html',
                  {'pk': article, 'authors': authors_list})
