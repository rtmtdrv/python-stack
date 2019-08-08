from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        "all_books": Book.objects.all(),
    }
    return render(request, "books_authors_app/index.html", context)

def add(request):
    Book.objects.create(title=request.POST["title"], desc=request.POST["desc"])
    return redirect("/")

def show(request, number):
    book_info = Book.objects.get(id=int(number))
    book_authors = book_info.authors.all()
    all_authors = Author.objects.all()
    context = {
        "book_info_html" : book_info,
        "book_authors_html" : book_authors,
        "all_authors_html" : all_authors,
    }
    return render(request, "books_authors_app/bookinfo.html", context)

def add_author(request, number):
    book_id = int(number)
    add_author_id = int(request.POST["author"])

    c = Book.objects.get(id=book_id)
    d = Author.objects.get(id = add_author_id)
    c.authors.add(d)
    
    return redirect(f"/books/{number}")
    
def show_authors(request):
    context = {
        "all_authors": Author.objects.all(),
    } 
    return render(request, "books_authors_app/authors.html", context)

def new_author(request):
    Author.objects.create(first_name=request.POST['f_name'], last_name=request.POST['l_name'], notes=request.POST['notes'],)
    return redirect("/authors")

def author_info(request, number):
    author_info = Author.objects.get(id=int(number))
    author_books = author_info.books.all()
    all_books = Book.objects.all()
    context = {
        "author_info_html" : author_info,
        "author_books_html" : author_books,
        "all_books_html" : all_books,
    }
    return render(request, "books_authors_app/authorinfo.html", context)

def add_book(request, number):
    author_id = int(number)
    add_book_id = int(request.POST["book"])

    c = Author.objects.get(id=author_id)
    d = Book.objects.get(id=add_book_id)
    c.books.add(d)

    return redirect(f"/authors/{number}")




