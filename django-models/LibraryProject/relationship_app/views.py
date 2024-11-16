from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library


#Create Views here
#Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

#Class_based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

