```python

>>> from bookshelf.models import Book
>>> book1 = Book.objects.get(pk=1) #saving book to be deleted in variable
>>> book1 #confirming that instance exists
<Book: 'Nineteen Eighty-Four' by George Orwell>
>>> book1.delete() #deleting the book
(1, {'bookshelf.Book': 1})
>>> Book.objects.all() #confirming that book does not exist in the db
<QuerySet []>

