from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from devices.views import (
    search, device_models_list, api_get_device
)
from menu.views import menu

apiVersion = 'v1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu),
    # path('menu/', menu, name='template-list'),
    path('search/', search, name='device-list'),
    path('device/<id>/models', device_models_list),
    path(apiVersion + '/device/<id>', api_get_device),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
