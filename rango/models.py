from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):

    NAME_MAX_LENGTH = 128

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Page(models.Model):

    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200
    
    def __str__(self):
        return self.title

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField(max_length=URL_MAX_LENGTH)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    