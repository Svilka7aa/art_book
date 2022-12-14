from django.contrib.auth import get_user_model
from django.shortcuts import render


UserModel = get_user_model()


def index(request):
    return render(request, 'common/index.html')

