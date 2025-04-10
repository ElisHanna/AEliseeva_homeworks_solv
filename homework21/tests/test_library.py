import os
import pytest
import logging
from apps.library import Book, Reader

os.system('cls')

logger = logging.getLogger()


@pytest.fixture
def book_one():
    return Book('Her', 'J.Doe', '150', '0001')


@pytest.fixture
def book_two():
    return Book('Him', 'J.Doe', '100', '0002')


@pytest.fixture
def reader_one():
    return Reader('Geralt')


@pytest.fixture
def reader_two():
    return Reader('Lyutik')


def test_reserve(book_one):
    assert book_one.reserve() == f'{book_one.title} by {book_one.author} is successfully booked'
    assert book_one.status == 'booked'
    logger.info('Test test_reserve passed')


def test_cancel_reserve(book_one):
    book_one.status = 'booked'
    assert book_one.cancel_reserve() == 'Your booking was successfully cancelled'
    assert book_one.status == 'available'
    assert book_one.cancel_reserve() is None
    logger.info('Test test_cancel_reserve passed')


def test_get_book(book_one, book_two):
    book_one.status = 'booked'
    book_two.status = 'available'
    assert book_one.get_book() == 'User got the book'
    assert book_two.get_book() == 'User got the book'
    assert book_one.status == 'borrowed'
    assert book_two.status == 'borrowed'
    assert book_one.get_book() is None
    assert book_two.get_book() is None
    logger.info('Test test_get_book passed')


def test_return_book(book_one, book_two):
    book_one.status = 'borrowed'
    assert book_one.return_book() == f'{book_one.title} by {book_one.author} is available now'
    assert book_two.return_book() is None
    logger.info('Test test_return_book passed')


def test_reserving_book(book_one, reader_one, reader_two):
    assert reader_one.reserving_book(book_one) is None
    assert book_one.title in reader_one.booked
    assert book_one.status == 'booked'
    assert reader_one.reserving_book(book_one) == 'User has already booked this book'
    assert reader_two.reserving_book(book_one) == \
           f'{book_one.title} by {book_one.author} is not available. Choose another book.'
    logger.info('Test test_reserving_book passed')


def test_cancelling_reserve(reader_one, reader_two, book_one):
    book_one.status = 'booked'
    reader_one.booked = [book_one.title]
    assert reader_two.cancelling_reserve(book_one) == 'User did not reserve this book'
    assert reader_one.cancelling_reserve(book_one) is None
    assert book_one.title not in reader_one.booked
    logger.info('Test test_cancelling_reserve passed')


def test_getting_book(book_one, book_two, reader_one, reader_two):
    book_one.status = 'booked'
    reader_one.booked = [book_one.title]
    assert reader_one.getting_book(book_one) is None
    assert book_one.title not in reader_one.booked
    assert book_one.title in reader_one.borrowed
    assert book_one.status == 'borrowed'
    assert reader_two.getting_book(book_one) == \
           f'{book_one.title} by {book_one.author} is not available. Choose another book.'
    assert book_two.status == 'available'
    assert book_two.title not in reader_two.booked
    assert book_two.title not in reader_two.borrowed
    assert reader_two.getting_book(book_two) is None
    assert book_two.title in reader_two.borrowed
    logger.info('Test test_getting_book passed')


def test_returning_book(book_one, book_two, reader_one, reader_two):
    book_one.status = 'borrowed'
    reader_one.borrowed = [book_one.title]
    book_two.status = 'booked'
    reader_two.booked = [book_two.title]
    assert reader_one.returning_book(book_one) is None
    assert book_one.title not in reader_one.borrowed
    assert reader_one.returning_book(book_two) == 'User did not borrow this book'
    assert reader_two.returning_book(book_two) == 'User did not borrow this book'
    logger.info('Test test_returning_book passed')
