from django.contrib import admin
from .models import Movie, Author, Review

# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)