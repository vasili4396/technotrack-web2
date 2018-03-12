from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='Post:post-detail',
        read_only=True
    )
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = CustomUser(
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
        fields = ('url', 'id', 'username',
                  'password', 'first_name', 'last_name',
                  'email', 'posts'
                  )
        # extra_kwargs = {
        #     'url': {
        #         'view_name': 'User:user-detail',
        #     }
        # }

# from .models import CustomUser
# from rest_framework import serializers
#
#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'username', 'is_staff')
