import os
import unittest
from library import Book, Reader

os.system('cls')


class TestLibrary(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.book_one = Book('Her', 'J.Doe', '150', '0001')
        cls.book_two = Book('Him', 'J.Doe', '100', '0002')
        cls.reader_one = Reader('Pelageya')
        cls.reader_two = Reader('Kondrati')

    def test_areserve(self):
        self.assertEqual(TestLibrary.book_one.reserve(),\
        f'{self.book_one.title} by {self.book_one.author} is successfully booked')
        self.assertIsNone(TestLibrary.book_one.reserve())

    def test_bcancel_reserve(self):
        self.assertEqual(TestLibrary.book_one.cancel_reserve(),\
        'Your booking was successfully cancelled')
        self.assertIsNone(TestLibrary.book_two.cancel_reserve())

    def test_cget_book(self):
        self.assertEqual(TestLibrary.book_one.get_book(),\
        'User got the book')
        self.assertIsNone(TestLibrary.book_one.get_book())

    def test_dreturn_book(self):
        self.book_one.status = 'borrowed'
        self.assertEqual(TestLibrary.book_one.return_book(),\
        f'{self.book_one.title} by {self.book_one.author} is available now')
        self.assertIsNone(TestLibrary.book_two.return_book())

    def test_ereserve_book(self):
        self.book_one.status = 'available'
        self.assertEqual(TestLibrary.reader_one.reserve_book(self.book_one),\
        self.book_one.reserve())
        self.assertEqual(TestLibrary.reader_two.reserve_book(self.book_two),\
        self.book_two.reserve())
        self.assertIn(self.book_one.title, self.reader_one.booked)
        self.assertNotIn(self.book_one.title, self.reader_two.booked)
        self.assertNotIn(self.book_one.title, self.reader_one.borrowed)
        self.assertNotIn(self.book_one.title, self.reader_two.borrowed)
        self.assertEqual(TestLibrary.reader_one.reserve_book(self.book_one),\
        'User has already booked this book')
        self.assertEqual(TestLibrary.reader_two.reserve_book(self.book_one),\
        f'{self.book_one.title} by {self.book_one.author} is not available. Choose another book.')

    def test_fcancel_reserve(self):
        self.assertEqual(TestLibrary.reader_two.cancel_reserve(self.book_one),\
        'User did not reserve this book')
        self.assertEqual(TestLibrary.reader_one.cancel_reserve(self.book_two),\
        'User did not reserve this book')
        self.assertEqual(TestLibrary.reader_one.cancel_reserve(self.book_one),\
        self.book_one.cancel_reserve())
        self.assertNotIn(self.book_one.title, self.reader_one.booked)
        self.assertEqual(TestLibrary.reader_one.cancel_reserve(self.book_one),\
        'User did not reserve this book')

    def test_get_book(self):
        self.assertEqual(TestLibrary.reader_one.get_book(self.book_two),\
        f'{self.book_two.title} by {self.book_two.author} is not available. Choose another book.')
        self.assertIn(self.book_two.title, self.reader_two.booked)
        self.assertEqual(TestLibrary.reader_two.get_book(self.book_two),\
        self.book_two.get_book())
        self.assertNotIn(self.book_two.title, self.reader_two.booked)
        self.assertIn(self.book_two.title, self.reader_two.borrowed)
        self.assertEqual(TestLibrary.reader_one.get_book(self.book_one),\
        self.book_one.get_book())
        self.assertIn(self.book_one.title, self.reader_one.borrowed)

    def test_return_book(self):
        self.assertEqual(TestLibrary.reader_one.return_book(self.book_one),
        self.book_one.return_book())
        self.assertNotIn(self.book_one.title, self.reader_one.borrowed)
        self.assertNotIn(self.book_one.title, self.reader_one.booked)
        self.assertEqual(TestLibrary.reader_one.return_book(self.book_two),\
        'User did not borrow this book')
        self.assertEqual(TestLibrary.reader_one.return_book(self.book_one),\
        'User did not borrow this book')
        self.assertNotEqual(TestLibrary.reader_two.return_book(self.book_two),\
        'User did not borrow this book')


if __name__ == '__main__':
    unittest.main()
