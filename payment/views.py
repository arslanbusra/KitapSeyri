import json
import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PaymentOrder, OrderItem
from buybook.models import BuyCart, BuyCartItem

@login_required
def checkout(request):
    cart, created = BuyCart.objects.get_or_create(user=request.user)
    cart_items = BuyCartItem.objects.filter(cart=cart)
    total_amount = sum(item.book.price * item.quantity for item in cart_items)

    # Iyzico ödeme işlemi için gerekli ayarlar
    api_key = 'sandbox-UklcsVGBCIVcUhOGdcWch5QBed3IBXC8'
    secret_key = 'sandbox-jXwn4PSVB7TUgRb25B0TsZow0NYbyRbr'
    base_url = 'https://sandbox-api.iyzipay.com'
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(api_key),
    }

    # Iyzico ödeme isteği oluşturma
    payment_request = {
        'locale': 'tr',
        'conversationId': '123456789',
        'price': str(total_amount),
        'paidPrice': str(total_amount),
        'currency': 'TRY',
        'installment': 1,
        'basketId': 'B67832',
        'paymentChannel': 'WEB',
        'paymentGroup': 'PRODUCT',
        'callbackUrl': 'http://127.0.0.1:8000/payment/complete/',
        'buyer': {
            'id': 'BY789',
            'name': request.user.first_name,
            'surname': request.user.last_name,
            'identityNumber': '74300864791',
            'email': request.user.email,
            'registrationAddress': 'Adres',
            'ip': '85.34.78.112',
            'city': 'Istanbul',
            'country': 'Turkey',
            'zipCode': '34732'
        },
        'shippingAddress': {
            'contactName': 'Jane Doe',
            'city': 'Istanbul',
            'country': 'Turkey',
            'address': 'Adres',
            'zipCode': '34732'
        },
        'billingAddress': {
            'contactName': 'Jane Doe',
            'city': 'Istanbul',
            'country': 'Turkey',
            'address': 'Adres',
            'zipCode': '34732'
        },
        'basketItems': [
            {
                'id': 'BI101',
                'name': item.book.bookname,
                'category1': item.book.booktype.name,
                'itemType': 'PHYSICAL',
                'price': str(item.book.price)
            } for item in cart_items
        ]
    }
    
    response = requests.post(
        f"{base_url}/payment/auth",
        headers=headers,
        data=json.dumps(payment_request),
        verify=False
    )

    payment_result = response.json()
    
    context = {
        'payment_result': payment_result,
        'cart_items': cart_items,
        'total_amount': total_amount,
    }
    
    return render(request, 'checkout.html', context)

@login_required
def complete(request):
    cart, created = BuyCart.objects.get_or_create(user=request.user)
    cart_items = BuyCartItem.objects.filter(cart=cart)
    order = PaymentOrder.objects.create(user=request.user, total_amount=sum(item.book.price * item.quantity for item in cart_items))
    
    for item in cart_items:
        OrderItem.objects.create(order=order, book=item.book, quantity=item.quantity)

    cart_items.delete()
    return redirect('profile')

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

