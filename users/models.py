from django.contrib.auth.models import AbstractUser
from django.forms import CharField


class Admin(AbstractUser):
    phone = CharField(max_length=13)

