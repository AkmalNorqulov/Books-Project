from django.shortcuts import render
from django.views.generic import *
# Create your views here.
from .models import *

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'
    
class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'
    
class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'