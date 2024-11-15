from django.shortcuts import render
from .models import Book 


#Create Views here
#Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})