from django.db.models import Avg
from .models import Review






def get_movie_recommendations(user):
    """
    Recommend based on similar user ratings.
    """
    # Get all movies rated by user
    user_reviews = Review.objects.filter(user=user).values_list("movie_title", flat=True)

    # Find users who've reviewed the same movies
    similar_users = Review.objects.filter(movie_title__in=user_reviews).exclude(user=user).values_list("user", flat=True).distinct()

    # Find movies that similar users liked (rated 4 or 5)
    recommended_movies = Review.objects.filter(
        user__in=similar_users, rating__gte=5
    ).exclude(movie_title__in=user_reviews).values("movie_title").annotate(avg_rating=Avg("rating")).order_by("-avg_rating")

    return [movie["movie_title"] for movie in recommended_movies]

    
    