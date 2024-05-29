from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserListSerializers, UserCreateSerializers, UserRetrieveSerializers


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    permission_classes = AllowAny,
    serializer_class = UserListSerializers


class MyProfileAPIView(RetrieveUpdateAPIView):
    model = User
    serializer_class = UserRetrieveSerializers

    def get_object(self):
        return self.request.user
