from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth.decorators import permission_required, login_required
from .forms import ExampleForm

# Create your views here.
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'book': books})

def create_book(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            return redirect('book_list') # Redirects to book list after saving
        else:
            form = ExampleForm # Create a blank form

        return render(request, 'bookshelf/book_form.html', {'form': form})

def raise_exception(request):
    
   raise Exception("This book is not in the library")  

