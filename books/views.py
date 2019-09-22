from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from books.models import Book


def index(request):
    return render(request, 'books/books.html')


class BookView(DetailView):
    template_name = 'books/book-view.html'
    model = Book
    context_object_name = 'book'

