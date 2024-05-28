from django.contrib.auth.models import AbstractUser
from django.db import models


class Admin(AbstractUser):
    phone = models.CharField(max_length=13)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Admins'


class Teacher(Admin):
    class Meta:
        proxy = True


class Moderator(Admin):
    class Meta:
        proxy = True


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    country = models.ForeignKey('apps.Country', models.CASCADE)
    description = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=40, null=True, blank=True)
    parol = models.CharField(max_length=30)
    image = models.ImageField(upload_to='user/%Y/%m/%d/', null=True, blank=True)

