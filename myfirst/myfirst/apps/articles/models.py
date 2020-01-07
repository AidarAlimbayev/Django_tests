import datetime
from django.db import models

from django.utils import timezone

class Article(models.Model):
    article_title = models.CharField(("article name"), max_length=200)
    article_text = models.TextField("article text")
    pub_date = models.DateTimeField(("date publication"), auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >=(timezone.now() - datetime.timedelta(days = 7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField(("author name"), max_length=50)
    comment_text = models.CharField(("text commentor"), max_length=200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
    