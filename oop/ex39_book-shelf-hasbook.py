#!/usr/bin/env python3

class Book():
    """A book class has title, author and price."""

    def __init__(self, title, author, price=0):
        self.title = title
        self.author = author
        self.price = price


class Shelf():
    """A book shielf class contains the books."""
    def __init__(self):
        self.books = []

    def add_new_books(self, *books_to_add):
        """Add new book to the shelf."""
        for book in books_to_add:
            self.books.append(book)

    def total_price(self):
        """Total price for the books on the shelf."""
        return sum(book.price for book in self.books)

    def has_book(self, title_name):
        """Return Ture or False for a book given the title name."""
        return title_name in (book.title for book in self.books)
        '''
        if title_name in [book.title for book in self.books]:
            print(f"found the book named {title_name}.")
            return True
        else:
            print("book not found.")
            return False
        '''


b1 = Book("python", "david", 15)
b2 = Book("java", "jenny", 10)

shelf = Shelf()
shelf.add_new_books(b1, b2)

print(f"Total price is {shelf.total_price()}")
print(shelf.has_book("Java"))
