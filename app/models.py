from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField('生徒名', max_length=200)
    submitdate = models.DateTimeField('投稿日', default=timezone.now)
    date = models.DateField(default=timezone.now)
    text = models.TextField('振替理由')

    def __str__(self):
        return self.title


class File(models.Model):
    name = models.CharField('ファイル名', max_length=255)
    src = models.FileField('添付ファイル')
    target = models.ForeignKey(
        Post,
        verbose_name='紐づく記事',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
