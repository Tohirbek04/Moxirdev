from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline

from apps.models import CourseVideo, Course, CustomGroup


class CourseVideoStackedInline(StackedInline):
    model = CourseVideo
    extra = 0
    min_num = 1


@admin.register(Course)
class CourseModelAdmin(ModelAdmin):
    inlines = CourseVideoStackedInline,
    filter_horizontal = 'groups',


@admin.register(CustomGroup)
class Group(ModelAdmin):
    filter_horizontal = 'users',
