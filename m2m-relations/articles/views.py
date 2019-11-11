from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    mymy={'title':'fignya','text':'this is nasha erunda'}
    articles_data = Article.objects.all()
    context = {'object_list':articles_data}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    #ordering = '-published_at'

    return render(request, template, context)
