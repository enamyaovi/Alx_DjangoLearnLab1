```python

>>> from bookshelf.models import Book
>>> book1 = Book(title='1984', author='George Orwell', publication_year=1949)
>>> book1.save()

# >>> from bookshelf.models import Book
# >>> Book.objects.create(title='1984', author='George Orwell', publication_year=1949)
# #output: <Book: '1984' by George Orwell>
