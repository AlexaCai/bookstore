from django.urls import path
from .views import BookListView
from .views import BookDetailView

app_name = 'books'

urlpatterns = [
    path('list/', BookListView.as_view(), name='list'),
    # Making the book titles clickable and telling Django which book’s details must be loaded \
    # involves the additional <pk> parameter. This parameter indicates the primary key of the object.
    path('list/<pk>', BookDetailView.as_view(), name='detail'),
]