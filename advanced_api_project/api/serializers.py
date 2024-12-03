from .models import Book, Author
from rest_framework import serializers
from datetime import date 

# Book Serializer
class BookSerializer(serializer.ModelSerializer):
    class Meta:
        model = Book
        fields = '_all_'

def validate_publication_year(self, value):
    """
    Ensure the publication_year in not in the future
    """
    current_year = date.today().year
    if value > current_year:
        raise serializers.ValidationError("Publication Year cannot be in the future.")
    return value


# Author Serializer
class AuthorSerializer(serializer.ModelSerializer):
    books = BookSerializer(many = True, read_only = True):

    class Meta :
        models = Author
        fields = ['name', 'books']