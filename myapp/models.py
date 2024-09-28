from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)  # Assuming ISBN-13 format

    def __str__(self):
        return self.title


# Create your models here.
