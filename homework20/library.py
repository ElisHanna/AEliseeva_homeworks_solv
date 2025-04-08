import os

os.system('cls')


class Book:

    def __init__(self, title, author, num_pages, isbn):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.status = 'available'

    def reserve(self):
        if self.status == 'available':
            self.status = 'booked'
            return f'{self.title} by {self.author} is successfully booked'

    def cancel_reserve(self):
        if self.status == 'booked':
            self.status = 'available'
            return 'Your booking was successfully cancelled'

    def get_book(self):
        if self.status in ('booked', 'available'):
            self.status = 'borrowed'
            return 'User got the book'

    def return_book(self):
        if self.status == 'borrowed':
            self.status = 'available'
            return f'{self.title} by {self.author} is available now'


class Reader:

    def __init__(self, name):
        self.name = name
        self.booked = []
        self.borrowed = []

    def reserve_book(self, book):
        if book.title in self.booked:
            return 'User has already booked this book'
        elif book.status == 'available':
            self.booked.append(book.title)
            book.reserve()
        else:
            return f'{book.title} by {book.author} is not available. Choose another book.'

    def cancel_reserve(self, book):
        if book.title in self.booked:
            self.booked.remove(book.title)
            book.cancel_reserve()
        else:
            return 'User did not reserve this book'

    def get_book(self, book):
        if book.title in self.booked:
            self.booked.remove(book.title)
            self.borrowed.append(book.title)
            book.get_book()
        elif book.status == 'available':
            self.borrowed.append(book.title)
            book.get_book()
        else:
            return f'{book.title} by {book.author} is not available. Choose another book.'

    def return_book(self, book):
        if book.title in self.borrowed:
            self.borrowed.remove(book.title)
            book.return_book()
        else:
            return 'User did not borrow this book'
