from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View

from store.models import Book, Order


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


class OrderSummaryView(View, LoginRequiredMixin):

    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, is_ordered=False)
            context = {
                'object': order
            }
        except ObjectDoesNotExist:
            messages.warning(self.request, "You don't have an active order")
            return redirect("/")

        return render(self.request, 'order_summary.html', context)
