from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Tags


def articles_list(request):
    template = 'articles/news.html'


    articles_data = Article.objects.all()
    all_tags = Tags.objects.all()
    print(all_tags)
    context = {'object_list':articles_data, 'tagslist': all_tags}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    #ordering = '-published_at'



    return render(request, template, context)
