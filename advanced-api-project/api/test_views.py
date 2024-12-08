from rest_framework import status 
from rest_framework.test import APITestCase
from .models import Book, Author
from .serializers import BookSerializer
from django.contrib.auth.models import User


class BookCreateTestCase(APITestCase):
    def test_create_book(self):
        user = User.objects.create(user = "Raymond", password = '7353634@duew')
        author = Author.objects.create(name = "Sigagala Hesborn")
        book = Book.objects.create(
            title  = "When The Dew Meets The Grass",
            author = author,
            publication_year = 2012
        )
        data = {
            'title': book.title,
            'author': book.author.pk,
            'publication_year': book.publication_year
        }
        response = self.client.post("books/create", data = data)
        self.assertEqual(response.data['title'], data['title'])
        self.assertDictEqual(response.status_code, 200)

    def test_update_book(self):
        user = User.objects.create(user = "Raymond", password = '7353634@duew')
        author = Author.objects.create(name = "Sigagala Hesborn")
        book = Book.objects.create(
            title  = "When The Dew Meets The Grass",
            author = author,
            publication_year = 2012
        )
        data = {
            'title': book.title,
            'author': book.author.pk,
            'publication_year': book.publication_year
        }
        self.client.login(username = user.username, password = self.user.password)
        response = self.client.post("books/update", data = data)
        self.assertEqual(response.status_code, 200)
        self.book.refresh_from_db
        self.assertEqual(response.data['title'], data['title'])
        

    def test_delete_book(self):
        response = self.client.post('books/delete/<int:pk>')
        self.assertEqual(response.status_code, 200)
        



