from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
# ListView to display list of all books 
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] 
    filterset_fields = ['title', 'author', 'publication_year'] # Fields for filtering
    search_fields = ['title', 'author'] # Define fields for search
    ordering_fields = ['title', 'publication_year'] # Define fields for ordering


#CreateView reders form to create a new book and only authenticated users can create a book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
#Detailview displays details of a specific book and any user can access book details
class BookDetailView(generics.RetrieveAPIView):
    queryset  = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

#UpdateView renders a form to update an existing book and only authenticated users can update book
class BookUpdateView(generics.UpdateAPIView):
    queryset  = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = IsAuthenticated

# DeleteView confirms and deletes a book and only authenticated users can destroy book
class BookDeleteView(generics.DestroyAPIView):
    queryset  = Book.objects.all()
    serializer_class = BookSerializer 
    permission_classes = [IsAuthenticated]