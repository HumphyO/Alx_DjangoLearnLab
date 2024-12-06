from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class User(models.Model):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    bio = models.TextField(max_length=270, blank=True)


# Comment model for users to read and authenticated users to post edit and delete comments
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)



    
