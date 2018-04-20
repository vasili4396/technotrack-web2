from rest_framework import serializers
from Post.models import Post
from User.serializers import SimpleUserSerializer


# TODO: likes and comments
class PostSerializer(serializers.ModelSerializer):
    author = SimpleUserSerializer(read_only=True)

    class Meta:
        model = Post

        fields = (
                    'url', 'author', 'title', 'created_at',
                    'text', 'comments_count', 'likes_count',
                 )

        read_only_fields = ('comments_count', 'likes_count', )
