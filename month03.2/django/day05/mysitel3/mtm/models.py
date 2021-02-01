from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField('作者',max_length=50)
    class Meta:
        verbose_name_plural='作者'
    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField('书名',max_length=50)
    authors=models.ManyToManyField(Author)
    class Meta:
        verbose_name_plural='书'
    def __str__(self):
        return self.title
