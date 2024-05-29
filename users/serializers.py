from rest_framework.serializers import ModelSerializer

from users.models import User


class UserListSerializers(ModelSerializer):

    class Meta:
        model = User
        fields = 'first_name', 'last_name'


class UserRetrieveSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'birthdate', 'phone', "country", "description", "email"


class UserCreateSerializers(ModelSerializer):

    class Meta:
        model = User
        fields = 'phone', 'password', 'first_name', 'last_name', 'username'
