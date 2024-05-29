from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import Country, User, AdminProxyModel, TeacherProxyModel, StudentProxyModel


@admin.register(User)
class UserModelAdmin(UserAdmin):
    autocomplete_fields = 'country',

    fieldsets = (
        (("Personal info"), {"fields": ("first_name", "last_name", "email", "phone", "image", "type", "gender",
                                        "country", "description",)}),
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


@admin.register(Country)
class CountryModelAdmin(admin.ModelAdmin):
    search_fields = 'name',


@admin.register(AdminProxyModel)
class AdminProxyModelAdmin(admin.ModelAdmin):
    pass


@admin.register(TeacherProxyModel)
class TeacherProxyModelAdmin(admin.ModelAdmin):
    pass


@admin.register(StudentProxyModel)
class StudentProxyModelAdmin(admin.ModelAdmin):
    pass
