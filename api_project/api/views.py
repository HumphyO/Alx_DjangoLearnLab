from rest_framework.generics import ListAPIView
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, IsAdminUser



# Create your views here.
class BookList (generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [ObtainAuthToken]
    permission_classes = [IsAuthenticated, IsAdminUser]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [ObtainAuthToken]
    permission_classes = [IsAuthenticated, IsAdminUser]


