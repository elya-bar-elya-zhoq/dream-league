from django.db import models

# Create your models here.

class suggestion(models.Model):
    suggestion_name = models.CharField(max_length=50)
    suggestion_text = models.TextField()
    suggestion_date = models.DateTimeField('date published')

    def __str__(self):
        return self.suggestion_name

    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'

class news(models.Model):
    news_name = models.CharField(max_length=50)
    news_text = models.TextField()
    news_date = models.DateTimeField('date published')

    def __str__(self):
        return self.news_name

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'