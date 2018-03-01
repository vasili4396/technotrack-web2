from django.contrib import admin
from .models import Comment
from .signals import *


def comment_delete(modeladmin, request, queryset):
    for obj in queryset:
        if obj.to_show:
            obj.to_show_iwant = False
            obj.save()


def comment_update(modeladmin, request, queryset):
    for obj in queryset:
        if not obj.to_show:
            obj.to_show_iwant = True
            obj.save()


comment_delete.short_description = "Not to show"
comment_update.short_description = "Show"


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_at', 'author_id',
                    'object_id', 'content_type_id', 'to_show')

    fieldsets = (
        (None, {
            'fields': ('text', 'author', 'content_type', 'object_id', )
        }),
    )
    actions = [comment_delete, comment_update]


admin.site.register(Comment, CommentAdmin)
