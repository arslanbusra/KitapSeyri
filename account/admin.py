from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile
from payment.models import PaymentOrder, OrderItem

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

# Admin paneline kullanıcı modelini ekle
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Admin paneline profil modelini ekle
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_email', 'user_first_name', 'user_last_name']

    def user_email(self, obj):
        return obj.user.email

    def user_first_name(self, obj):
        return obj.user.first_name

    def user_last_name(self, obj):
        return obj.user.last_name

    user_email.short_description = 'Email'
    user_first_name.short_description = 'First Name'
    user_last_name.short_description = 'Last Name'

# PaymentOrder modelini admin paneline ekle
@admin.register(PaymentOrder)
class PaymentOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_amount', 'created_at']

# OrderItem modelini admin paneline ekle
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'book', 'quantity']