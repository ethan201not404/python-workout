#!/usr/bin/env python3

class Book():
    """Solution to chapter 9, exercise 39, beyond 2: has_book"""

    def __init__(self, title, author, price=0, width=5):
        self.title = title
        self.author = author
        self.price = price
        self.width = width


class Shelf():
    """A shelf class has all the books."""

    def __init__(self, width):
        self.width = width
        self.books = []

    def add_new_books(self, *new_books):
        for book in new_books:
            if book.width + self.get_book_width() > self.width:
                raise "Too many book"
            self.books.append(book)

    def total_price(self):
        return sum(book.price for book in self.books)

    def has_book(self, title_name):
        return title_name in (book.title for book in self.books)

    def get_book_width(self):
        return sum(book.width for book in self.books)


b1 = Book("python", "david", 15)
b2 = Book("java", "jenny", 10)

shelf = Shelf(9)
shelf.add_new_books(b1, b2)

print(f"Total price is {shelf.total_price()}")
print(shelf.has_book("java"))

print(shelf.get_book_width())
