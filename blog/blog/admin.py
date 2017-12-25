from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post
from .models import Blog

admin.site.register(Post)

class PostAdmim(admin.ModelAdmin):
    list_display = 'name', 'createdata'

admin.site.register(Blog)