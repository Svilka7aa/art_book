from django.shortcuts import render, redirect
from django.urls import reverse

from art_book.photos.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm
from art_book.photos.models import Photo


def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST)
        if form.is_valid():
            art = form.save(commit=False)
            art.user = request.user
            art.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'photo/add_photo.html', context)


def details_photo(request, pk):
    photo = Photo.objects.filter(pk=pk) \
        .get()

    user_liked_photo = Photo.objects.filter(pk=pk, user_id=request.user.pk)

    context = {
        'photo': photo,
        'has_user_liked_photo': user_liked_photo,
        'likes_count': photo.photolike_set.count(),
        "is_owner": request.user == photo.user,
    }

    return render(
        request,
        'photo/photo-details.html',
        context,
    )


def get_post_photo_form(request, form, success_url, template_path, pk=None):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(success_url)

    context = {
        'form': form,
        'pk': pk,
    }

    return render(request, template_path, context)


def edit_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    return get_post_photo_form(
        request,
        PhotoEditForm(request.POST or None, instance=photo),
        success_url=reverse('index'),
        template_path='photo/edit-photo.html',
        pk=pk,
    )


def delete_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    return get_post_photo_form(
        request,
        PhotoDeleteForm(request.POST or None, instance=photo),
        success_url=reverse('index'),
        template_path='photo/delete-photo.html',
        pk=pk,
    )
