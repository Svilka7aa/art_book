from django.urls import path

from art_book.common.views import index

urlpatterns = [
    path('', index, name="index"),
]
