from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

# 博客文章数据模型
class ArticlePost(models.Model):
    # 文章作者。
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    total_views = models.PositiveIntegerField(default=0)
    # 文章标题。
    title = models.CharField(max_length=100)

    # 文章正文。
    body = models.TextField()

    # 文章创建时间。
    created = models.DateTimeField(default=timezone.now)

    # 文章更新时间。
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)

    def __str__(self):
        # 将文章标题返回
        return self.title
    # 获取文章地址
    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])
