from django.shortcuts import render, redirect

from art_book.photos.forms import PhotoCreateForm


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


def details_photo():
    pass


def edit_photo():
    pass


def delete_photo():
    pass
