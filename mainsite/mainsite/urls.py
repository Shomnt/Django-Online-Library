from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('reader/', include('reader.urls')),
    path('', include('base.urls')),
    path('admin/', admin.site.urls),
]
