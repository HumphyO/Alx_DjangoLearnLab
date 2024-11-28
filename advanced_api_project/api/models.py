from django.db import models

# Create your models here.
# Author model
class Author(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

# Book model
class Book(models.model):
    title = models.CharField(max_length = 150)
    publication_year = models.DateField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name = 'books')

    def __str__(self):
        return self.title