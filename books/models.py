from django.db import models
from django.shortcuts import reverse


# Create your models here.

genre_choices= (
('action', 'Action'),
('adventure', 'Adventure'),
('biography', 'Biography'),
('classic', 'Classic'), 
('comic', 'Comic'), 
('cookbook', 'Cookbook'),
('crime', 'Crime'), 
('educational', 'Educational'),
('essay', 'Essay'), 
('fantasy', 'Fantasy'),
('graphic novel', 'Graphic novel'), 
('history', 'History'), 
('historical fiction', 'Historical fiction'),
('horror', 'Horror'), 
('memoir', 'Memoir'), 
('mystery', 'Mystery'),
('poetry', 'Poetry'), 
('romantic', 'Romantic'), 
('self-development', 'Self-development'), 
('science fiction', 'Science fiction'), 
('thriller', 'Thriller'),
('other', 'Other'),
)

book_type_choices=(
('hardcover','Hardcover'),
('paperback','Paperback'),
('ebook', 'E-Book'),
('audiobook', 'Audiobook')
)

language_choices=(
('english','English'),
('french','French'),
('spanish', 'Spanish'),
)

class Book (models.Model):
    title = models.CharField(max_length=120)
    author_name = models.CharField(max_length=120)
    genre = models.CharField(max_length=20, choices=genre_choices, default='classic')
    summary = models.TextField(max_length=1000, default='')
    book_type = models.CharField(max_length=12, choices=book_type_choices, default='hardcopy')
    language = models.CharField(max_length=20, choices=language_choices, default='english')
    price = models.FloatField(help_text= 'in US dollars $')
    pic = models.ImageField(upload_to='books', default='no_picture.jpg')

    # Function that take <pk> as the primary key and generate a URL
    def get_absolute_url(self):
       return reverse ('books:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.title)
