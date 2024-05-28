from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from users.permissions import IsOwner
from users.serializers import UserListSerializes, UserCreateSerializers, UserSerializers
from users.models import User


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = AllowAny,

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserListSerializes
        return UserCreateSerializers


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = IsOwner,

