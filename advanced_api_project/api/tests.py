from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Book
from rest_framework import status

# Create your tests here.
class BookAPITest(APITestCase):
    def test_create_book(self):
        data = {'title': 'Test Book', 'author': 'Test Author', 'publication_year': ()}
        response = self.client.post(f"/books/create", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), )

    def test_update_book(self):
        # Test the UpdateView 
        data = {"title": "Updated Book One", "author": "Author A", "publication_date": ''}
        response = self.client.put(f"/books/{self.book1.id}/update/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book One")
        
    def test_delete_book(self):
        # Test the DeleteView (DELETE /books/<id>/delete/)
        response = self.client.delete(f"/books/{self.book1.id}/delete/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)  # Two books should be deleted
   