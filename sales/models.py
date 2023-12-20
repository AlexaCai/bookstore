from django.db import models
from books.models import Book # because we need to connect sales with books - this come from the Book app

# Create your models here.

class Sale (models.Model):

    # 'CASCADE' implies that when a book is deleted all the positions related to the book will be deleted
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
	    return f"id: {self.id}, book: {self.book}, quantity: {self.quantity}, price: {self.price}, created_at: {self.date_created}"
