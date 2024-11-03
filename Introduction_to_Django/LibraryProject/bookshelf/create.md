from bookshelf.models import Book

# python command
python manage.py shell

# Create book instance
book = Book.objects.create(title = "1984", author = "George Orwell", publication_year =1949)
book.save()

# Expected output
