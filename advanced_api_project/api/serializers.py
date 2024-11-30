from rest_framework import serializers
from .models import Book, Author
from datetime import date

# Book serializer
class BookSerializer(serializers.ModelSerializer):
    class meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Validation to ensure publication_year is not in the future
        """    
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("The publication year must match the current year.")
        return value

# Author serializer
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many = True, read_only = True)

    class meta:
        model = Author
        fields = 'name, books'