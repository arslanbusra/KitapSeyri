from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('complete/', views.complete, name='complete'),
    path('cart/', views.cart, name='cart'),
]
