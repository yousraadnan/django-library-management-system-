


from django.shortcuts import render, redirect
from urllib3 import request

from .models import Book
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def add_book(request):
    if request.method == 'POST':
        title =request.POST.get('bookTitle')
        author = request.POST.get('bookAuthor')
        genre = request.POST.get('bookGenre')
        published_date =request.POST.get('publishedDate')
        isbn = request.POST.get('bookISBN')

        # Debugging print statement
        print(f'Title: {title}, Author: {author}, Genre: {genre}, Date: {published_date}, ISBN: {isbn}')


        new_book = Book(
            title= title,
            author=author,
            genre=genre,
            published_date=published_date,
            isbn=isbn
        )
        print("About to save the book...")
        new_book.save()
        print("Book saved successfully.")
        # Save the book to the database
        return redirect('home')


    return render(request, 'add_new_book.html')

def book_list(request):
    books = Book.objects.all()  # Get all books
    return render(request, 'book_list.html', {'books': books})