﻿```python

>>> from bookshelf.models import Book
>>> Book.objects.create(title='1984', author='George Orwell', publication_year=1949)
# Output: <Book: '1984' by George Orwell>
>>> Book.objects.all()
#Output: <QuerySet [<Book: '1984' by George Orwell>]>
>>> Book.objects.values_list('pk', 'title')
#Output: <QuerySet [(1, '1984')]>
>>> book1 = Book.objects.get(pk=1) 
>>> book1
<Book: '1984' by George Orwell>
>>> book1.title
# Output: '1984'
>>> book1.author
# Output: 'George Orwell'
>>> book1.publication_year
# Output: 1949
>>> book1.title = 'Nineteen Eighty-Four'
>>> book1     
#Output: <Book: 'Nineteen Eighty-Four' by George Orwell>
>>> book1.save()
>>> Book.objects.get(pk=1) 
#Output: <Book: 'Nineteen Eighty-Four' by George Orwell>
>>> book1.delete()
# Output: (1, {'bookshelf.Book': 1})
>>> Book.objects.all()
# Output: <QuerySet []>

