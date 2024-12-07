from django.db import models

# Create your models here.
# Author model for DataBase
class Author(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

# Book Model for DataBase
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title