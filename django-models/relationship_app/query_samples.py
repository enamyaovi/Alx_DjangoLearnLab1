from models import Author, Book, Librarian, Library

#retrieving an author from the Author Table with pk of 2
author2 = Author.objects.get(pk=2)
print(author2.name)

#retrieving the books by that author
author2_books = Book.objects.all().filter(author__name=author2.name)
for book in author2_books:
    print(f"{book.title}")

#retrieving a Library in database
library_name = 'ALX' # assumming library exists in database
# mylibrary = Library.objects.get(pk=1)
mylibrary = Library.objects.get(name=library_name)
mylibrary_books = mylibrary.books.all()

for book in mylibrary_books:
    print(f"Book: '{book.title}', written by: {book.author}")

#retrieving the Librarian at mylibrary
print(f"{mylibrary.librarian.name} works at {mylibrary.name}")
