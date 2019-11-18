from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField('Tags', through='Scopes')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tags(models.Model):

    name = models.CharField(max_length=30, verbose_name='тэги')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


class Scopes(models.Model):
    is_main = models.BooleanField(default=False, verbose_name='основное')

    article = models.ForeignKey(Article, related_name='scope', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, related_name='scope', on_delete=models.CASCADE)


