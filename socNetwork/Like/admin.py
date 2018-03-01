from django.contrib import admin
from .models import Like


def like_delete(modeladmin, request, queryset):
    for obj in queryset:
        if obj.to_show:
            obj.save()


def like_update(modeladmin, request, queryset):
    for obj in queryset:
        if not obj.to_show:
            obj.save()


like_delete.short_description = "Not to show"
like_update.short_description = "Show"


class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_id', 'content_type_id', 'object_id', 'to_show')

    fieldsets = (
        (None, {
            'fields': ('author', 'content_type', 'object_id', )
        }),
    )
    actions = [like_delete, like_update]


admin.site.register(Like, LikeAdmin)
