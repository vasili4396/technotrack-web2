from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from category.models import Category

admin.site.register(Category)