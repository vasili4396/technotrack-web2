from rest_framework import serializers
from Comment.models import Comment
from django.contrib.contenttypes.models import ContentType
from User.serializers import SimpleUserSerializer
from Post.models import Post


# TODO: доделать для других объектов
class TaggedObjectRelatedFeild(serializers.RelatedField):
    def to_representation(self, value):
        request = self.context.get('request', None)
        if isinstance(value, Post):
            from Post.serializers import PostSerializer
            serializer = PostSerializer(value, context={'request': request})
        # elif isinstance(value, Comment):
        #     serializer = CommentSerializer(value, context={'request': request})
        # if isinstance(value, Event):
            # serializer = EventSerializer(value, context={'request': request})
        else:
            # return SimpleCommentSerializer(value.all(), many=True)
            return value.__str__()
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    author = SimpleUserSerializer(read_only=True)
    content_type = serializers.SlugRelatedField(queryset=ContentType.objects.all(), slug_field='model')
    object = TaggedObjectRelatedFeild(read_only=True)

    class Meta:
        model = Comment

        fields = ('id', 'text', 'author', 'to_show', 'created_at', 'likes_count', 'content_type', 'object', 'object_id')
        read_only_fields = ('id', 'to_show', 'created_at', 'likes_count',)


class SimpleCommentSerializer(serializers.RelatedField):
    author = SimpleUserSerializer(read_only=True)

    def to_representation(self, value):
        request = self.context.get('request', None)
        if isinstance(value, ):
            from Post.serializers import PostSerializer
            serializer = PostSerializer(value, context={'request': request})
        elif isinstance(value, Comment):
            serializer = CommentSerializer(value, context={'request': request})
            # if isinstance(value, Event):
            # serializer = EventSerializer(value, context={'request': request})
        else:
            return value.__str__()
        return serializer.data

    class Meta:
        model = Comment
        fields = ('id', 'created_at', 'author')
