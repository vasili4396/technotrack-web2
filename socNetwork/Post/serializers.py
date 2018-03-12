from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Post

        fields = ('url', 'author', 'title', 'created_at', 'text')
        extra_kwargs = {
            'url': {
                'view_name': 'Post:post-detail',
            }
        }
