from django.contrib.auth import get_user_model
from django.shortcuts import render

UserModel = get_user_model()


def home_page(request):
    users = UserModel.objects.all()
    context = {
        'users': users,
    }

    return render(request, 'common/home_page.html', context)
