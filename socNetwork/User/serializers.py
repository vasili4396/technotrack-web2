from rest_framework import serializers, status
from .models import CustomUser
from rest_framework.exceptions import ValidationError


class SimpleUserSerializer(serializers.ModelSerializer):
    avatar = serializers.StringRelatedField(many=True)

    class Meta:
        model = CustomUser
        fields = ('url', 'username', 'email', 'avatar')
        read_only_fields = ('id', 'email',)
        extra_kwargs = {
            'url': {
                'lookup_field': 'username'
            },
        }


class UserChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def update(self, instance, validated_data):
        if not instance.check_password(validated_data.get('old_password')):
            raise ValidationError({"old_password": ["wrong password"]}, code=status.HTTP_400_BAD_REQUEST)
        if not (validated_data.get('password') == validated_data.get('confirm_password')):
            raise ValidationError({"confirm_password": ["passwords dont match"]}, code=status.HTTP_400_BAD_REQUEST)
        instance.set_password(validated_data.get("password"))
        instance.save()
        return instance

    class Meta:
        model = CustomUser

        fields = (
            'old_password', 'password', 'confirm_password',
        )


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.StringRelatedField(many=True)

    def update(self, instance, validated_data):
        for field in validated_data:
            instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance

    class Meta:
        model = CustomUser

        fields = ('id', 'username',
                  'first_name', 'last_name',
                  'email', 'last_login', 'sex',
                  'city', 'date_of_birth',
                  'country', 'avatar'
                  )
        read_only_fields = ('id', 'email', 'last_login')


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    avatar = serializers.StringRelatedField(many=True)

    def create(self, validated_data):
        if validated_data.get('username', None) == '':
            username = None
        else:
            username = validated_data.get('username')
        user = CustomUser(
            email=validated_data.get('email', None),
            first_name=validated_data.get('first_name', None),
            last_name=validated_data.get('last_name', None),
            username=username
        )
        user.set_password(validated_data.get('password', None))
        user.save()
        if username is None:
            user.__class__.objects.filter(pk=user.id).update(username='id' + str(user.id))
        return user

    class Meta:
        model = CustomUser

        fields = ('email', 'password', 'username',
                  'first_name', 'last_name', 'avatar'
                  )
