from django.db import models
from django.contrib.auth.models import User, AbstractUser, UserManager
from django.conf import settings



# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

class Tag(models.Model):
    name = models.CharField(max_length=200)


class CustomUserManager(UserManager):
    def create_user(self, email = ..., password = ..., **extra_fields):
        if not email:
            raise ValueError("Email field required")
        user = self.create_user(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password)
        user.is_staff= True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class CustomUser(AbstractUser):
    username= models.CharField(unique=True, max_length=130)
    email = None

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    bio = models.TextField()
    picture = models.URLField(max_length=180, blank=True)


# Comment model for users to read and authenticated users to post edit and delete comments
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)






    
