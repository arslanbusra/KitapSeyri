from django.contrib import admin
from django.urls import path, include
from homepage import views as homepage_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_views.index, name='index'),
    path('about/', homepage_views.about, name='about'),
    path('contact/', homepage_views.contact, name='contact'),
    path('sellbook/', include('sellbook.urls')),
    path('buybook/', include('buybook.urls')),
    path('article/', include('article.urls')),
    path('activity/', include('activity.urls')),
    path('account/', include('account.urls')), 
    path('payment/', include('payment.urls')), 

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

