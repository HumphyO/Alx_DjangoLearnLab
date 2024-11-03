# python command
python manage.py shell

# Retrieve all books
all_books = Book.objects.all()

# Retrieve specific book
book = Book.objects.get(title="1984)
