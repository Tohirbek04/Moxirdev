from django.db import models
from django.template.defaultfilters import slugify


class BaseModel(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Category(BaseModel):
    class Meta:
        verbose_name_plural = 'Categories'


class Country(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)


class Course(models.Model):
    title = models.CharField(max_length=30)
    price = models.FloatField(db_default=0.0)
    description = models.TextField()
    category = models.ForeignKey('apps.Category', models.CASCADE)

    def __str__(self):
        return self.title


class CourseVideo(models.Model):
    video = models.FileField(upload_to='course/%Y/%m/%d/')
    course = models.ForeignKey('apps.Course', models.CASCADE)
