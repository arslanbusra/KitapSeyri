from django.db import models
from django.contrib.auth.models import User
from sellbook.models import SellBook
from payment.models import PaymentOrder

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sold_books = models.ManyToManyField(SellBook, blank=True, related_name='sold_books')
    orders = models.ManyToManyField(PaymentOrder, blank=True,related_name='orders')
    past_events = models.ManyToManyField('activity.Event', blank=True, related_name='past_events')
    upcoming_events = models.ManyToManyField('activity.Event', blank=True, related_name='upcoming_events')

    def __str__(self):
        return self.user.username

