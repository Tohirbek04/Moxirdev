from rest_framework.serializers import ModelSerializer

from users.models import User


class UserListSerializes(ModelSerializer):
    class Meta:
        model = User
        fields = 'first_name', 'last_name',


class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        exclude = 'parol',


class UserCreateSerializers(ModelSerializer):
    class Meta:
        model = User
        exclude = 'id',

