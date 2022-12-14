from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model

from art_book.accounts.forms import UserCreateForm

UserModel = get_user_model()


class LogIn(auth_views.LoginView):
    template_name = "profile/login.html"
    next_page = reverse_lazy('index')


class Register(views.CreateView):
    template_name = 'profile/register.html'
    form_class = UserCreateForm
    success_url = reverse_lazy("index")

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response


class LogOut(auth_views.LogoutView):
    template_name = 'profile/'
    # model = UserModel
    next_page = reverse_lazy('index')


class ProfileDetails(views.DetailView):
    template_name = "profile/profile.html"
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        name = self.request.user.first_name + " " + self.request.user.last_name
        email = self.request.user.email

        context['name'] = name
        context['email'] = email
        context['is_owner'] = self.request.user == self.object
        context["art_count"] = self.object.art_set.count

        photos = self.object.photo_set.all().prefetch_related("photolike_set")

        context["photos_cunt"] = photos.count
        # TODO fix the likes
        # context['likes_count'] = sum(x.photolike_set.count() for x in photos)

        return context


class ProfileEditView(views.UpdateView):
    template_name = 'profile/edit-profile.html'
    model = UserModel
    fields = ("first_name", "last_name", "email")

    def get_success_url(self):
        return reverse_lazy("profile details", kwargs={
            "pk": self.request.user.pk,
        })


class ProfileDeleteView(views.DeleteView):
    template_name = 'profile/delete-profile.html'
    model = UserModel
    success_url = reverse_lazy('index')
