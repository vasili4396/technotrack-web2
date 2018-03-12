from rest_framework import serializers
from .models import CustomUser
from Post.models import Post
from rest_framework.generics import get_object_or_404
from rest_framework import reverse


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # def get_posts(self, validated_data):
    #     posts = Post.objects.filter(author_id=validated_data.get('id', None))
    #     return posts.values('id')
    #
    # class CustomHyperLinkedField(serializers.HyperlinkedRelatedField):
    #     def get_object(self, view_name, view_args, view_kwargs):
    #         queryset = self
    #         object = get_object_or_404()
    #
    #     class Meta:
    #         model = Post

    # post = CustomHyperLinkedField(
    #     view_name='Post:post-detail',
    #     read_only=True,
    # )
    password = serializers.CharField(write_only=True)
    email = serializers.ReadOnlyField()

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data.get('email', None),
            first_name=validated_data.get('first_name', None),
            last_name=validated_data.get('last_name', None),
            username=validated_data.get('username', None)
        )
        user.set_password(validated_data.get('password', None))
        user.save()
        return user

    def update(self, instance, validated_data):
        for field in validated_data:
            if field == 'password':
                instance.set_password(validated_data.get(field))
            else:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance

    class Meta:
        model = CustomUser

        fields = ('url', 'id', 'password', 'username',
                  'first_name', 'last_name',
                  'email',
                  )

        extra_kwargs = {
            'url': {
                'view_name': 'User:customuser-detail',
            },
            'id': {
                'read_only': True
            },
            'email': {
                'read_only': True
            },
        }

# from .models import CustomUser
# from rest_framework import serializers
#
#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'username', 'is_staff')
