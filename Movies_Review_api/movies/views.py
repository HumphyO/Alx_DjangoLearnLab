from django.shortcuts import render
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework.response import Response


# Create your views here.
# Movie API view
class MovieAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    

class ReviewCreateView(CreateAPIView):
     queryset = Review.objects.all()
     serializer_class = ReviewSerializer
     permission_classes = [IsAuthenticated]


     def create(self, serializer):
        serializer.save(director=self.requets.user)

class ReviewDetailView(RetrieveAPIView):
    queryset =Review.objects.all()
    serializer_class= ReviewSerializer
    permission_classes= [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(director=self.request.user)

