from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from users.models import User


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'username', 'image'


class UserRetrieveSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'birthdate', 'phone', "country", "description", "email"


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'phone', 'email', 'password')

    def create(self, validated_data):
        user = super(UserCreateSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

