from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Post
from Comment.models import Comment
from Like.models import Like

# TODO: сделать чтобы при "удалении" поста, флаги на привязанных коментах и лайках ставились на False


def post_delete(modeladmin, request, queryset):
    for obj in queryset:
        if obj.to_show:
            obj.to_show = False
            obj.save(update_fields=['to_show'])


def post_update(modeladmin, request, queryset):
    for obj in queryset:
        if not obj.to_show:
            obj.to_show = True
            obj.object.__class__.objects.get(pk=obj.object_id).update(to_show=True)
            obj.save(update_fields=['to_show'])


post_delete.short_description = "Not to show"
post_update.short_description = "Show"


class CommentInline(GenericTabularInline):
    model = Comment


class LikeInline(GenericTabularInline):
    model = Like


class PostAdmin (admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'created_at', 'updated_at', 'author_id', 'comments_count', 'likes_count', 'to_show')

    fieldsets = (
        (None, {
            'fields': ('text', 'title', 'author', )
        }),
    )

    inlines = [
            CommentInline,
            LikeInline
    ]

    actions = [post_delete, post_update]


admin.site.register(Post, PostAdmin)
