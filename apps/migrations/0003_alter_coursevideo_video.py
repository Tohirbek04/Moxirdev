# Generated by Django 5.0.6 on 2024-05-30 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_course_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursevideo',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='course'),
        ),
    ]
