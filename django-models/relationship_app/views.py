from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library


# Create your views here.
#Function_based view 
def list_books(request):
    books = Book.objects.all() #Retrieve all books from datbase
    return render(request, 'relationship_applist_books.html',{'books': books})

