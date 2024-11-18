from django.shortcuts import render, redirect
from sellbook.models import Category, SellBook
from .models import BuyCart, BuyCartItem
from django.contrib.auth.decorators import login_required

def buybook(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        books = SellBook.objects.filter(booktype_id=category_id)
    else:
        books = SellBook.objects.all()

    context = {
        'categories': categories,
        'books': books
    }
    return render(request, 'buybook.html', context)

@login_required
def add_to_cart(request, book_id):
    book = SellBook.objects.get(id=book_id)
    cart, created = BuyCart.objects.get_or_create(user=request.user)
    cart_item, created = BuyCartItem.objects.get_or_create(cart=cart, book=book)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def cart(request):
    cart, created = BuyCart.objects.get_or_create(user=request.user)
    cart_items = BuyCartItem.objects.filter(cart=cart)
    total_amount = sum(item.book.price * item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_amount': total_amount,
    }
    return render(request, 'cart.html', context)


@login_required
def update_cart(request, item_id):
    cart_item = BuyCartItem.objects.get(id=item_id)
    if request.method == 'POST':
        quantity = request.POST['quantity']
        cart_item.quantity = quantity
        cart_item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = BuyCartItem.objects.get(id=item_id)
    if request.method == 'POST':
        cart_item.delete()
    return redirect('cart')



