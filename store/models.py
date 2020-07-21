from django.db import models
from django.conf import settings
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    is_ordered = models.BooleanField(default=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.book.title}"

    def get_total_book_price(self):
        return self.quantity * self.book.price


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    books = models.ManyToManyField(OrderItem)
    created_at = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total_amount(self):
        total = 0
        for order_item in self.books.all():
            total += order_item.get_total_book_price()
        return total
