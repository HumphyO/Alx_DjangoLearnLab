from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# Retrieving all books Read_only accessible to everyone
class BookListView(ListAPIView):
   queryset= Book.objects.all()
   serializer_class = BookSerializer

# Retrieving a single book ID Read_only accessible to everyone
class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Adding a new book for authenticated users only
class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes= [IsAuthenticated]

# Modifying an existing book for authenticated users only
class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Removing a book for authenticated users only
class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]