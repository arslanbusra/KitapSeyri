from django.contrib import admin
from django.urls import path, include
from homepage import views as homepage_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_views.index, name='index'),
    path('about/', homepage_views.about, name='about'),
    path('contact/', homepage_views.contact, name='contact'),
    path('sellbook/', homepage_views.sellbook, name='sellbook'),
    path('buybook/', include('buybook.urls')),
    path('article/', include('article.urls')),
    path('activity/', include('activity.urls')),
    path('account/', include('account.urls')), 

]


