from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book, Publisher
# Create your views here.

def index(request):
    author_list = Author.objects.all()
    book_list = Book.objects.all()
    publisher_list = Publisher.objects.all()

    html = "Author:  <br/><br/>"
    for a in author_list:
        html = html + str(a.id) + ":" + a.first_name + ' ' + a.last_name + "<br/><br/>"

    html = html + "<br>Books:<br/><br/>"
    for book in book_list:
        html = html + str(book.id) + ":" + book.title + "<br/><br/>"

    html = html + "<br>Publisher:<br/><br/>"
    for p in publisher_list:
        html = html + str(p.id) + ":" + p.name + "<br/><br/>"
    return HttpResponse(html)
# Create your views here.

def detail(request, book_id):
    #author_list = Author.objects.all()
    book = Book.objects.get(id=book_id)
    html = str(book.id)+ ":" + book.title + "<br/><br/>"
    html = html + " Published by:" + str(book.publisher) + "<br/><br/>"
    html = html + " Published at:" + str(book.publication_date)
    return HttpResponse(html)

def author_detail(request, author_id):
    a = Author.objects.get(id=author_id)
    html = "author details: " + a.first_name + " " + a.last_name + "<br/><br/>"
    html = html + " Email Address: " + a.email
    return HttpResponse(html)
