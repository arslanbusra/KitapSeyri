from django.contrib import admin
from .models import  Category, Language, BuyBook, BuyCart, BuyCartItem


admin.site.register(Category)
admin.site.register(Language)
admin.site.register(BuyBook)
admin.site.register(BuyCart)
admin.site.register(BuyCartItem)



