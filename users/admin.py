from django.contrib import admin
from django.contrib.admin import action
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from users.models import Country, User
from users.proxy import AdminProxyModel, TeacherProxyModel, StudentProxyModel, ModeratorProxyModel
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class BaseUserAdmin(UserAdmin):
    autocomplete_fields = 'country',
    list_display = 'id', 'username', 'show_image'
    filter_horizontal = ['groups', 'user_permissions']
    fieldsets = (
        (None, {"fields": ("username", "password", "phone", "country")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "is_staff", "is_superuser")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("My photo"), {"fields": ("show_image", "image")}),
    )
    readonly_fields = ['show_image']

    @action(description='Photo')
    def show_image(self, obj: User):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100px" height="100px" alt="">')
        return 'No image'


@admin.register(AdminProxyModel)
class AdminProxyModelAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password", "phone", "country")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "description")}),
        (_("Permissions"),
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
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("My photo"), {"fields": ("show_image", "image")}),
    )

    def save_model(self, request, obj, form, change):
        obj.type = User.Type.ADMIN
        obj.is_superuser = True
        super().save_model(request, obj, form, change)


@admin.register(TeacherProxyModel)
class TeacherProxyModelAdmin(BaseUserAdmin):

    def save_model(self, request, obj, form, change):
        obj.type = User.Type.TEACHER
        super().save_model(request, obj, form, change)


@admin.register(StudentProxyModel)
class StudentProxyModelAdmin(BaseUserAdmin):

    def save_model(self, request, obj, form, change):
        obj.type = User.Type.STUDENT
        super().save_model(request, obj, form, change)


@admin.register(ModeratorProxyModel)
class ModeratorProxyModelAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password", "phone", "country")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "is_staff")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("My photo"), {"fields": ("show_image", "image")}),
    )

    def save_model(self, request, obj, form, change):
        obj.type = User.Type.MODERATOR
        obj.is_staff = True
        super().save_model(request, obj, form, change)


@admin.register(Country)
class CountryAdminModel(admin.ModelAdmin):
    search_fields = 'name',
