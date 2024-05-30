from users.managers import AdminProxyManager, StudentProxyManager, TeacherProxyManager, ModeratorProxyManager
from users.models import User


class AdminProxyModel(User):
    objects = AdminProxyManager()

    class Meta:
        proxy = True
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'


class StudentProxyModel(User):
    objects = StudentProxyManager()

    class Meta:
        proxy = True
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class TeacherProxyModel(User):
    objects = TeacherProxyManager()

    class Meta:
        proxy = True
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class ModeratorProxyModel(User):
    objects = ModeratorProxyManager()

    class Meta:
        proxy = True
        verbose_name = 'Moderator'
        verbose_name_plural = 'Moderators'
