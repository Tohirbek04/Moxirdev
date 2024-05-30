from rest_framework import permissions

from apps.models import Course


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Course):
        for i in obj.groups.all():
            if request.user in i.users.all():
                return True

