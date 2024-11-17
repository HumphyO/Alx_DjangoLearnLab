from relationship_app.models import Author, Book, Library, Librarian 

#Function to query all books by specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)  # Fetch the author by name
    books = Book.objects.filter(author=author)  # Filter books by the author
    return books

#Function to list all books in a library
def get_library_books(library_name):
    return Library.objects.get(name=library_name).books.all()

#Function to relate librarian to library
def get_librarian_for_library(library_name):
    Library.objects.get(name=library_name)# Fetch the library by name
    Librarian.objects.get(library=Library) # Fetch the librarian by library instance
    return Librarian