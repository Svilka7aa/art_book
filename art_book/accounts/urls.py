from django.urls import path, include

from art_book.accounts.views import ProfileDetails, LogIn, Register, LogOut, ProfileEditView, ProfileDeleteView

#
urlpatterns = (
    path('login/', LogIn.as_view(), name='login user'),
    path('register/', Register.as_view(), name='register user'),

    path("profile/<int:pk>/", include([
        path("", ProfileDetails.as_view(), name="profile details"),
        path("logout/", LogOut.as_view(), name="logout user"),
        path("edit/", ProfileEditView.as_view(), name="profile edit"),
        path("delete/", ProfileDeleteView.as_view(), name="profile delete"),
    ])),
)
