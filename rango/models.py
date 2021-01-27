from django.db import models

class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

class Page(models.Model):
    
    def __str__(self):
        return self.title

    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    