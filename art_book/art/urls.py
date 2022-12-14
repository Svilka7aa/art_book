from django.urls import path, include

from art_book.art.views import add_art, details_art, edit_art, delete_art

urlpatterns = (
    path('add/', add_art, name='add art'),


    # TODO: to fix it when users are done
    # path('<str:username>/art/<slug:art_slug>/', include([
    path('art/<slug:art_slug>/', include([
        path('', details_art, name='details art'),
        path('edit/', edit_art, name='edit art'),
        path('delete/', delete_art, name='delete art'),
    ]))
)