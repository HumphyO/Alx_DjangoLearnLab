from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library


#Create Views here
#Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

#Class_based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/librarry_detail.html'
    context_object_name = 'library'

