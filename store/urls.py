from django.urls import path

from store.services import add_to_cart
from store.views import book_list, BookDetailView


urlpatterns = [
    path('', book_list, name='book-list'),
    path('book/<slug>/', BookDetailView.as_view(), name='book'),
    path('add-to-cart/<slug>/', add_to_cart, name="add-to-cart")
]