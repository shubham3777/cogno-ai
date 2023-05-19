from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CreateUserForm, UserChangeForm
from django.contrib.auth.models import User


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(
                    request, f"Account created successfully for {user}")
                return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def loginView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Incorrect credentials")
                return redirect('login')
        return render(request, 'login.html')


def logoutView(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


def user_list(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users_list.html', context)

def delete_user(request, id):
    user = User.objects.get(id=id)
    print(user)
    user.delete()
    return redirect('user-list')