from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser


class Category(models.Model):

    title =models.CharField(
        verbose_name='カテゴリ',
        max_length=20
    )
    def __str__(self):
        return self.title
    
class PhotoPost(models.Model):


    user =models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )

    category =models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT
    )
    title =models.CharField(
        verbose_name='タイトル',
        max_length=200
    )
    comment =models.TextField(
        verbose_name='コメント'
    )
    image1 = models.ImageField(
        verbose_name='イメージ1',
        upload_to= 'photos'
    )
    image2 = models.ImageField(
        verbose_name='イメージ2',
        upload_to= 'photos',
        blank=True,
        null =True
    )
    posted_at =models.DateField(
        verbose_name='投稿日時',
        auto_now_add=True
    )
    def __str__(self):
        return self.title

from django.contrib.auth import get_user_model
class Comment(models.Model):
    TOPIC_CHOICES = [
        ('sf6', '>>sf6とは'),
        ('ruke', '>>ルークの使い方'),
        ('puzzle', '>>パズドラ'),
        ('question','>>質問')
        # 他のトピックも追加可能
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField(verbose_name='コメント')
    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES, verbose_name='トピック', default='general')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text} ({self.get_topic_display()})'



