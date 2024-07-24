from django.db import models
from django.contrib.auth.models import User
from sellbook.models import SellBook

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sold_books = models.ManyToManyField(SellBook, blank=True, related_name='sold_books')
    orders = models.ManyToManyField('buybook.Order', blank=True, related_name='user_orders')
    past_events = models.ManyToManyField('activity.Event', blank=True, related_name='past_events')
    upcoming_events = models.ManyToManyField('activity.Event', blank=True, related_name='upcoming_events')

    def __str__(self):
        return self.user.username


