from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library


# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html',{'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        conext = super().get_context_data(**kwargs)
        conext ['books'] = self.get_object.books.all()
        