from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Books(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Janr(models.Model):
    janr = models.CharField(max_length=50)
    book = models.ForeignKey(Books, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.janr
