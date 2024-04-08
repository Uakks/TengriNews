import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import Article
from .utils.get_tags import ArticleParser


# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-project_date')
    paginator = Paginator(articles, 15)
    page = request.GET.get('page')
    news = paginator.get_page(page)
    return render(request, 'index.html', {'articles': articles, 'news': news, 'tags': ArticleParser.get_tags()})


def news(request, pk):
    article = Article.objects.get(project_id=f"{pk}")
    auts = article.authors
    auths = auts.split("'")
    authors_list = []
    for author in auths:
        print(len(author))
        if len(author) > 2:
            authors_list.append(author)

    tags = article.project_tags.split("'")
    tags_list = set()
    for tag in tags:
        if len(tag) > 2:
            tags_list.add(tag)

    print(authors_list)
    return render(request, 'news.html',
                  {'pk': article, 'authors': authors_list, 'tags': tags_list})


def search_articles(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        filters = request.POST.getlist('filtered')
        # print(filters)
        # print(type(searched))
        if len(filters) >= 1 and searched is not None:
            articles = Article.objects.filter(title__icontains=searched, project_tags__icontains=filters[0])
            print(type(filters[0]))
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
