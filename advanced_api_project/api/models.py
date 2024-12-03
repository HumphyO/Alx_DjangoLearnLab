from django.db import models

# Create your models here.
# Author model creation
class Author(models.Model):
    name = models.CharField(max_length = 130)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 200)
    publication_year = models.DateField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE)

    def __str__(self):
        return self.title