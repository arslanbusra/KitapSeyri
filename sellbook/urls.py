from django.urls import path
from . import views

urlpatterns=[
    path('',views.sellbook, name="sellbook"),

    #path(route, view,opt(kisayolisim))

]