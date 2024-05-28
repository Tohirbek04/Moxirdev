from django.contrib import admin

from users.models import Admin, Teacher, Moderator, User


@admin.register(Admin)
class AdminModelAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email", "phone", "photo")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


@admin.register(Teacher)
class TeacherModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Moderator)
class ModeratorModelAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    pass
