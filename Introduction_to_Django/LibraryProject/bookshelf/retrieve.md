```python
>>> from bookshelf.models import Book
>>> Book.objects.all() #retrieving all book objects
#output: <QuerySet [<Book: '1984' by George Orwell>]>
>>> Book.objects.values_list('pk', 'title') #looking up books in the database and their primary keys
#output: <QuerySet [(1, '1984')]>
>>> book1 = Book.objects.get(pk=1) #retrieving the book instance with primary key 1
>>> book1
#output: <Book: '1984' by George Orwell>

#retrieving all book attributes
>>> book1.title
#output: '1984'
>>> book1.author
#output: 'George Orwell'
>>> book1.publication_year
#output: 1949
