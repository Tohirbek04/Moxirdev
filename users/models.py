from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices


class Country(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)

    def __str__(self):
        return self.name


class User(AbstractUser):
    class GenderType(TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'

    class Type(TextChoices):
        ADMIN = 'admin', 'Admin'
        STUDENT = 'student', 'Student'
        TEACHER = 'teacher', 'Teacher'

    type = models.CharField(max_length=20, choices=Type.choices, default=Type.STUDENT)
    image = models.ImageField(upload_to='user/%Y/%m/%d/', null=True, blank=True)
    phone = models.CharField(max_length=13, unique=True)
    birthdate = models.DateTimeField(null=True)
    gender = models.CharField(max_length=10, choices=GenderType.choices)
    country = models.ForeignKey('users.Country', models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class AdminProxyModel(User):
    class Meta:
        proxy = True
        verbose_name = 'Admin'


class StudentProxyModel(User):
    class Meta:
        proxy = True
        verbose_name = 'Student'


class TeacherProxyModel(User):
    class Meta:
        proxy = True
        verbose_name = 'Teacher'
