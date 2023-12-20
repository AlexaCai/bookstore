from django.test import TestCase
from .models import Book # to access Book model

# Create your tests here.

class BookModelTest(TestCase):
    def setUpTestData():
       # Set up non-modified objects used by all test methods
       Book.objects.create(title='Title1', author_name='Author1', genre='classic', book_type='hardcover', price='23.71')
       Book.objects.create(title='Title2', author_name='Author2', genre='classic', book_type='hardcover', price='23.71')
       Book.objects.create(title='Title3', author_name='Author3', genre='classic', book_type='hardcover', price='23.71')
       Book.objects.create(title='Title4', author_name='Author4', genre='classic', book_type='hardcover', price='23.71')
       Book.objects.create(title='Title5', author_name='Author5', genre='classic', book_type='hardcover', price='23.71')

    def test_book_title(self):
       # Get a book object to test
       book = Book.objects.get(id=1)

       # Get the metadata for the 'title' field and use it to query its data
       field_label = book._meta.get_field('title').verbose_name

       # Compare the value to the expected result
       self.assertEqual(field_label, 'title')

    def test_author_name_max_length(self):
        # Get a book object to test
        book = Book.objects.get(id=1)

        # Get the metadata for the 'author_name' field and use it to query its max_length
        max_length = book._meta.get_field('author_name').max_length

        # Compare the value to the expected result i.e. 120
        self.assertEqual(max_length, 120)

    def test_get_absolute_url(self):
       book = Book.objects.get(id=1)
       # get_absolute_url() should take to the detail page of book #1
       # and load the URL /books/list/1
       self.assertEqual(book.get_absolute_url(), '/books/list/1')

    def test_get_absolute_url(self):
       book = Book.objects.get(id=3)
       # get_absolute_url() should take to the detail page of book #3
       # and load the URL /books/list/3
       self.assertEqual(book.get_absolute_url(), '/books/list/3')

    def test_get_absolute_url(self):
       book = Book.objects.get(id=5)
       # get_absolute_url() should take to the detail page of book #5
       # and load the URL /books/list/5
       self.assertEqual(book.get_absolute_url(), '/books/list/5')