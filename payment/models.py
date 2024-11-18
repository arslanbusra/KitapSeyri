from django.db import models
from django.contrib.auth.models import User
from sellbook.models import SellBook

class PaymentOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.total_amount} ₺ - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

class OrderItem(models.Model):
    order = models.ForeignKey(PaymentOrder, on_delete=models.CASCADE)
    book = models.ForeignKey(SellBook, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.book.bookname} - Adet: {self.quantity} - Sipariş: {self.order.user.username}"



