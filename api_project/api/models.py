from django.db import models

# Create your models here.
class Book(models.model):
    title = models.CharField(max_length = 130)
    author = models.CharField(max_length = 200)
    publishing_date = models.DateField()
