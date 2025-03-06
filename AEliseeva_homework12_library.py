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
            print(f'The book{self.title} by {self.author} is successfully booked')
        else:
            print(f'The book {self.title} by {self.author} is not available. Choose another book.')


    def cancel_reserve(self):
        if self.status == 'booked':
            self.status = 'available'
            print(f'Your booking was successfully cancelled')



    def get_book(self):
        if self.status == 'booked' or self.status == 'available':
            self.status = 'borrowed'
            print('User got the book')


    def return_book(self):
        if self.status == 'borrowed':
            self.status = 'available'
            print(f'The book {self.title} by {self.author} is available now')


class Reader:


    def __init__(self, name):
        self.name = name
        self.booked = []
        self.borrowed = []


    def reserve_book(self, book):
        if book.title in self.booked:
            print('User has already booked this book')
        elif book.status == 'available':
            self.booked.append(book.title)
            book.reserve()
        else: book.reserve()


    def cancel_reserve(self, book):
        if book.title in self.booked:
            self.booked.remove(book.title)
            book.cancel_reserve()
        else:
            print('User did not reserve this book')


    def get_book(self, book):
        if book.title in self.booked:
            self.booked.remove(book.title)
            self.borrowed.append(book.title)
            book.get_book()
        elif book.status == 'available':
            self.borrowed.append(book.title)
            book.get_book()
        else:
            print(f'The book {book.title} by {book.author} is not available. Choose another book.')


    def return_book(self, book):
        if book.title in self.borrowed:
            self.borrowed.remove(book.title)
            book.return_book()
        else:
            print('User did not borrow this book')


harry_potter1 = Book("Harry Potter and dust on bookshelf", "J.K.Rowling", "150", "0000001")
harry_potter2 = Book("Harry Potter and secret of cheese", "J.K.Rowling", "200", "0000002")
harry_potter3 = Book("Harry Potter and mystery of OOP", "J.K.Rowling", "250", "0000003")
harry_potter4 = Book("Harry Potter and tetanus shot", "J.K.Rowling", "300", "0000004")
harry_potter5 = Book("Harry Potter and flat Earth society", "J.K.Rowling", "400", "0000005")
harry_potter6 = Book("Harry Potter and hair in the sink", "J.K.Rowling", "350", "0000006")
harry_potter7 = Book("Harry Potter and apology of Socrates", "J.K.Rowling", "300", "0000007")


john_doe = Reader('John Doe')
jane_doe = Reader('Jane Doe')

john_doe.reserve_book(harry_potter1)
jane_doe.reserve_book(harry_potter1)
jane_doe.reserve_book(harry_potter2)
john_doe.get_book(harry_potter1)
jane_doe.reserve_book(harry_potter1)
jane_doe.get_book(harry_potter1)
jane_doe.return_book(harry_potter1)
jane_doe.return_book(harry_potter2)
john_doe.return_book(harry_potter1)
jane_doe.cancel_reserve(harry_potter2)
