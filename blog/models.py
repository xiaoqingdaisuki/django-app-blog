from django.db import models
from django.contrib import admin
from django.urls import reverse
# Create your models here.

class BlogPost(models.Model):
	"""
    Django 要求模型必须继承 models.Model 类。
    CharField 指定了分类名 name 的数据类型，CharField 是字符型，
	"""
	#文章标题
	title = models.CharField(max_length = 100)
	#文章概括
	excerpt = models.CharField(max_length = 200, blank=True)
	#文章内容
	body = models.TextField()
	#编辑时间
	timestamp = models.DateTimeField()
	#文章编号
	text = models.CharField(max_length = 100,blank=True)

class Post(models.Model):
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:text', kwargs={'pk': self.pk})
