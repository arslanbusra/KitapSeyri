from django.contrib import admin
from .models import BuyBook, Category, Language, Order

admin.site.register(BuyBook)
admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Order)


