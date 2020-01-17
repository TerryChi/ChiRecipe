
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages

from recipe.models import User

from django.core.exceptions import ObjectDoesNotExist


def login(request):
    if request.method == "POST":
        reg_id = request.POST.get('reg_id', '')
        password = request.POST.get('password', '')


        try:
            user = auth.authenticate(username=reg_id, password=password)

            if user is None or not user.is_active:
                messages.error(request, 'ID : {} not found'.format(reg_id))
                return redirect('login')

            auth.login(request, user)
            messages.success(request, 'Login Success.')

        except ObjectDoesNotExist:
            return redirect('login')

        return redirect('/')
    else:
        return render(request, 'register/login.html')


# @login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout Success.')

    return redirect('homepage')


def user_register(request):
    if request.method == "POST":
        password = request.POST.get("password")
        password_check = request.POST.get("password_check")
        if password != password_check:
            messages.error(request, "Your password isn't match")
            return render(request, "user/user_create.html")
        name = request.POST.get("name")
        reg_id = request.POST.get("reg_id")
        user = User.objects.create_user(reg_id=reg_id, privilege=0)
        user.set_password(password)
        user.name = name
        user.save()
        return redirect('login')
    else:
        return render(request, 'user/user_create.html')
