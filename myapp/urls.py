from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_new_book.html', views.add_book, name='add_book'),
    path('book_list.html', views.book_list, name='book_list'),  # Route for searching books
]