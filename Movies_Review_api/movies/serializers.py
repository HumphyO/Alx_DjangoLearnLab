from .models import Movie, Review
from rest_framework import serializers
from django.contrib.auth.models import User

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["title", "genre", "title"]

class ReviewSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField(read_only=True)
    movie_title = serializers.CharField(source='movie.title', read_only=True)


    class Meta:
        model = Review
        fields = '__all__'

   

       
