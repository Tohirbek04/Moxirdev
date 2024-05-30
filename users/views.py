from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserListSerializer, UserRetrieveSerializers, UserCreateSerializer


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = AllowAny,

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserListSerializer
        return UserCreateSerializer


class MyProfileAPIView(RetrieveUpdateAPIView):
    model = User
    serializer_class = UserRetrieveSerializers

    def get_object(self):
        return self.request.user
