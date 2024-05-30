from rest_framework import permissions

from apps.models import Course


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Course):

        return request.user in obj.users.all()
