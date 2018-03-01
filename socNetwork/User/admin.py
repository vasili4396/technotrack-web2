from django.contrib import admin
from .models import CustomUser, Avatar
from django.contrib.contenttypes.admin import GenericTabularInline
from Comment.models import Comment
from Like.models import Like


class CommentInline(GenericTabularInline):
    model = Comment


class LikeInline(GenericTabularInline):
    model = Like


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_login', 'email', 'first_name', 'last_name', 'is_admin', 'avatar')


class AvatarAdmin(admin.ModelAdmin):
    list_display = ('id', 'likes_count', 'comments_count', 'avatar', 'user_id', 'to_show')

    fieldsets = (
        (None, {
            'fields': ('user', 'avatar', )
        }),
    )

    inlines = [
        CommentInline,
        LikeInline
    ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Avatar, AvatarAdmin)

