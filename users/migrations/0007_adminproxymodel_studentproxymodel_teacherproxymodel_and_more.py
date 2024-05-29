# Generated by Django 5.0.6 on 2024-05-29 09:38

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_birthdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminProxyModel',
            fields=[
            ],
            options={
                'verbose_name': 'Admin',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='StudentProxyModel',
            fields=[
            ],
            options={
                'verbose_name': 'Student',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TeacherProxyModel',
            fields=[
            ],
            options={
                'verbose_name': 'Teacher',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('admin', 'Admin'), ('student', 'Student'), ('teacher', 'Teacher')], default='student', max_length=20),
        ),
    ]
