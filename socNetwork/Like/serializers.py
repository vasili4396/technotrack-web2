from rest_framework import serializers
from .models import Like
from User.serializers import SimpleUserSerializer
#
#
# class AllLikeSerializer(serializers.ModelSerializer):
#     author = SimpleUserSerializer(read_only=True)
#
#     class Meta:
#         model = Like
#
#         fields = ('id', 'author', 'to_show', 'created_at',)


class ToShowLikeSerializer(serializers.ModelSerializer):
    author = SimpleUserSerializer(read_only=True)

    class Meta:
        model = Like

        fields = ('id', 'author', 'to_show', 'created_at',)
