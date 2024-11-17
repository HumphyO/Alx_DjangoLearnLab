from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import permission_required, login_required

# Create your views here.
@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'book': books})
def raise_exception(request):
    
   raise Exception("This book is not in the library")  

   