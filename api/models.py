from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    book_name = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.RESTRICT)
    description = models.TextField(null=True)