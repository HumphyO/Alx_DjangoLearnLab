from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
# User model
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=130)

    def __str__(self):
        return self.name
    
    
# Review Model
class Review(models.Model):
    movie_title = models.CharField(max_length=200, default='Unknown')
    review_content = models.TextField(default="")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    