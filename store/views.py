from django.shortcuts import render
from django.views.generic import ListView, DetailView

from store.models import Book


def book_list(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, "book_list.html", context)


class BookView(ListView):
    model = Book
    template_name = "book_list.html"


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_view.html'
