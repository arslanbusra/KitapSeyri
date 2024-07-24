from django.shortcuts import render
from sellbook.models import Category, SellBook  # Uygun modelleri içe aktarın

def buybook(request):
    categories = Category.objects.all()
    books = SellBook.objects.all()  # Satılan kitapları getirmek için

    context = {
        'categories': categories,
        'books': books
    }
    return render(request, 'buybook.html', context)


