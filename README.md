## Read Mate Web Application Backend

```
python manage.py shell

```


```
from api.models import *

author = Author.objects.create(name="J.K. Rowling", description="Author of the Harry Potter series")
book = Book.objects.create(book_name="Harry Potter and the Sorcerer's Stone", 
                           author=author, 
                           description="The first book in the Harry Potter series.")

```

```
author1 = Author.objects.create(name="George Orwell", description="Author of '1984' and 'Animal Farm'.")
author2 = Author.objects.create(name="J.R.R. Tolkien", description="Author of 'The Lord of the Rings' and 'The Hobbit'.")
author3 = Author.objects.create(name="Agatha Christie", description="The Queen of Crime, author of 'Murder on the Orient Express'.")


book1 = Book.objects.create(book_name="1984", author=author1, description="A dystopian novel set in a totalitarian society.")
book2 = Book.objects.create(book_name="Animal Farm", author=author1, description="A satirical allegory about the Russian Revolution.")


book3 = Book.objects.create(book_name="The Hobbit", author=author2, description="The prelude to 'The Lord of the Rings'.")
book4 = Book.objects.create(book_name="The Lord of the Rings: The Fellowship of the Ring", author=author2, description="The first book in 'The Lord of the Rings' trilogy.")


book5 = Book.objects.create(book_name="Murder on the Orient Express", author=author3, description="A detective novel featuring Hercule Poirot.")
book6 = Book.objects.create(book_name="The Murder of Roger Ackroyd", author=author3, description="A crime novel known for its controversial twist ending.")

```