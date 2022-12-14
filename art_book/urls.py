from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('art_book.common.urls')),
    path('accounts/', include('art_book.accounts.urls')),
    path('art/', include('art_book.art.urls')),
    path('photos/', include('art_book.photos.urls')),
]
