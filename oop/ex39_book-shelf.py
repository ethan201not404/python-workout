#!/usr/bin/env python3

"""A shelf class that contains the books."""


class Book():
    """A book class represents a book with title, author and price."""

    def __init__(self, title, author, price=0):
        self.titile = title
        self.author = author
        self.price = price


class Shelf():
    """A shelf class contains books.
    It can add book and get a total price of the books on the shelf.
    """

    def __init__(self):
        self.books_on_shelf = []

    def add_book(self, *books_to_add):
        """Add books to a shelf. *books_to_add a tuple of all books to add
        """
        for book in books_to_add:
            self.books_on_shelf.append(book)

    def total_price(self):
        """Return the total price"""
        # total = 0
        # for book in self.books_on_shelf:
        #     total += book.price
        # return total
        return sum(book.price for book in self.books_on_shelf)


b1 = Book("python", "david", 15)
b2 = Book("java", "jenny", 10)

shelf = Shelf()
shelf.add_book(b1, b2)

print(f"Total price is {shelf.total_price()}")
