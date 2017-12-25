# coding: utf-8
from django.db import models
from django.conf import settings
from category.models import Category


class Post(models.Model):
    postname = models.CharField(default='', max_length=255)
    text = models.TextField(default='')
    createdata = models.DateTimeField(auto_now_add=True)
    changedata = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    blog = models.ForeignKey('blog.Blog', related_name='posts')

    def __str__(self):
        return u'{} ({}) {}'.format(self.postname, self.author, self.text)


class Blog(models.Model):
    name = models.CharField(default='', max_length=255)
    createdata = models.DateTimeField(auto_now_add=True, editable=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.name


class Like(models.Model):
    post = models.ForeignKey('blog.Post', default=True, related_name='likes')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
