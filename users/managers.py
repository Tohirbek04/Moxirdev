from django.contrib.auth.models import UserManager


class AdminProxyManager(UserManager):

    def get_queryset(self):
        return super().get_queryset().filter(type=self.model.Type.ADMIN)


class ModeratorProxyManager(UserManager):

    def get_queryset(self):
        return super().get_queryset().filter(type=self.model.Type.MODERATOR)


class TeacherProxyManager(UserManager):

    def get_queryset(self):
        return super().get_queryset().filter(type=self.model.Type.TEACHER)


class StudentProxyManager(UserManager):

    def get_queryset(self):
        return super().get_queryset().filter(type=self.model.Type.STUDENT)

