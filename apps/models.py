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


