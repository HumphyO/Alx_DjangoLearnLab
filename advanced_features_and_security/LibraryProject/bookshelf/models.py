from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
    
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=130)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    class Meta:
        permissions = [
            ("can_add_book", "Can Add Book")
            ("can_change_book", "Can Change Book")
            ("can_delete_book", "Can Delete Book")
        ]

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

class CustomUser(AbstractUser):
    """Custom User Model that extends AbstractUser."""
    date_of_birth = models.DateField(blank = True, null = True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null = True, blank = True)


    def __str__(self):
        return self.username

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password = None, **extra_fields):
        if not email:
            raise ValueError("The Email Field must be set")
        email = self.normalize_email(email)
        user = self.model(username = username, email = email **extra_fields)
        user.set_passwords(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, username, email, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True.')
        
        return self.create_user(username, email, password, **extra_fields)