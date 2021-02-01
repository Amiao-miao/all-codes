from django.db import models

# Create your models here.

class Publisher(models.Model):
    name=models.CharField('出版社名',max_length=50,unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='出版社'
class Book(models.Model):
    name=models.CharField('书名',max_length=50)

    publisher=models.ForeignKey(Publisher,verbose_name='出版社',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='图书'
