from django.urls import path
from . import views

urlpatterns=[
    path('',views.buybook, name="buybook"),

    #path(route, view,opt(kisayolisim))

   

]