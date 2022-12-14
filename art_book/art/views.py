from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from art_book.art.forms import ArtCreateForm, ArtEditForm, ArtDeleteForm
from art_book.art.models import Art
from art_book.core.utils import is_owner


def get_art_by_name_and_username(art_slug, username):
    return Art.objects.filter(slug=art_slug, user__username=username).get()


@login_required
def add_art(request):
    if request.method == 'GET':
        form = ArtCreateForm()
    else:
        form = ArtCreateForm(request.POST)
        if form.is_valid():
            art = form.save(commit=False)
            art.user = request.user
            art.save()

            # TODO fix it to work with pk
            # return redirect('index', pk=request.user.pk)

            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'art/add_art.html', context)


def details_art(request, username, art_slug):
    return render(request, 'art/art-details.html')


def edit_art(request, username, art_slug):
    art = get_art_by_name_and_username(art_slug, username)
    if not is_owner(request, art):
        return redirect('details pet', username=username, art_slug=art_slug)

    if request.method == "GET":
        form = ArtEditForm(instance=art)
    else:
        form = ArtEditForm(request.POST, isnstance=art)
        if form.is_valid():
            form.save()
            return redirect('edit art', username=username, art_slug=art_slug)

    context = {
        "form": form,
        "art_slug": art_slug,
        "username": username,
    }

    return render(request, "art/edit-art.html", context)


def delete_art(request, username, art_slug):
    art = get_art_by_name_and_username(art_slug, username)

    if request.method == 'GET':
        form = ArtDeleteForm(instance=art)
    else:
        form = ArtDeleteForm(request.POST, instance=art)
        if form.is_valid():
            form.save()
            return redirect('details user', pk=1)

    context = {
        'form': form,
        'art_slug': art_slug,
        'username': username,
    }

    return render(
        request,
        'art/delete-art.html',
        context,
    )


