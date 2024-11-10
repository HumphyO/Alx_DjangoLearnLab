from relationship_app.models import Author, Book, Library, Librarian

#Function to query all books by specific author
def get_books_by_author(author_name):
    return Book.objects.filter(author_name=author_name)

#Function to list of all the books in library
def get_library_books(library_name):
    return Library.objects.get(name=library_name).books.all()

#Function to specify librarian of a library
def get_library_librarian(library_name):
    return Library.objects.get(name=library_name).librarian