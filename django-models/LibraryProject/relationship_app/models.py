from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=130)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library= models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class UserProfile(models.Model):
        #Roles choices
        Role_Choices= [
            ('Admin', 'Admin'),
            ('Librarian', 'Librarian'),
            ('Member', 'Member'),
        ]

        #Fields Required
        user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
        role = models.CharField(max_length=25, choices=Role_Choices, default='Member')

        def __str__(self):
            return f"{self.user.username} - {self.role}"
        

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)

