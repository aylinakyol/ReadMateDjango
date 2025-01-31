from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint 

class Author(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    book_name = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(null=True)

class FavoriteBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'book'], name='unique user book list')
        ]    