from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here
def index(request):
    return render(request, 'django_delights/index.html')


def home(request):
    if request.user.is_authenticated:
        return render(request, 'django_delights/home.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request=request,
            username = username,
            password= password
        )

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "Wrong username or password")
            return redirect('login_user')
    else:
        return render(request, 'django_delights/login.html')

def logout_user(request):
    logout(request)

    return redirect('index')