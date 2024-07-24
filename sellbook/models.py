from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SellBook(models.Model):
    bookname = models.CharField(max_length=255)
    authorname = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    booktype = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    booklang = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    bookimage = models.ImageField(upload_to='book_images/')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sell_books')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bookname

