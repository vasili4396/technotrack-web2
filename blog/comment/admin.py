from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Comment

admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = 'id','text', 'author', 'post',