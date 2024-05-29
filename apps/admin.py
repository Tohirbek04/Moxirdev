from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline

from apps.models import CourseVideo, Course


class CourseVideoStackedInline(StackedInline):
    model = CourseVideo
    extra = 0
    min_num = 1


@admin.register(Course)
class CourseModelAdmin(ModelAdmin):
    inlines = CourseVideoStackedInline,
    filter_horizontal = 'users',


