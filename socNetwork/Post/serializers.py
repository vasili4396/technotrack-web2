from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='User:customuser-detail'
    )

    class Meta:
        model = Post

        fields = ('url', 'author', 'title', 'created_at', 'text', 'comments_count')
        extra_kwargs = {
            'url': {
                'view_name': 'Post:post-detail',
            }
        }
