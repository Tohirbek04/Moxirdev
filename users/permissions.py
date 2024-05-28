from rest_framework import permissions

from users.models import User


class IsOwner(permissions.BasePermission):
    message = 'This account does not belong to you'

    def has_object_permission(self, request, view, obj: User):
        return obj.id == request.user.id