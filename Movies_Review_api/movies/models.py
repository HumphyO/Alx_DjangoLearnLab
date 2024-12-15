from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=130)
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Review(models.Model):
    RATING_CHOICES = [

        0, '0 - Very Poor',
        1, '1 - Poor',
        2, '2- Average',
        3, '3 - Good', 
        4, '4 - Very Good',
        5, '5 - Excellent',
    ]
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    director = models.ForeignKey()
    plot = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f'Review for {self.movie.title} by {self.director.username}'
    