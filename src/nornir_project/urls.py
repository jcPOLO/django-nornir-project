from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from devices.views import search
from menu.views import menu


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu),
    path('menu/', menu, name='template-list'),
    path('search/', search, name='device-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
