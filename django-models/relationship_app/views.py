from django.shortcuts import render

from .models import Book


# Create your views here.
#Function_based view 
def list_books(request):
    books = Book.objects.all() #Retrieve all books from datbase
    book_list = []
    for book in books:
        book_list.append(f"{book.title} by {book.author.name}")
    return render(request, 'relationship_app/list_books.html', {'books': books})

