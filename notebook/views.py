from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/user/')
    if request.method == "POST":
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
        # else:
        #     messages.error(request, "Registration Failed")
        return render(request, 'notebook/html/index.html', {'form': fm})
    fm = RegistrationForm()
    return render(request, 'notebook/html/index.html', {'form': fm})


def user_page(request):
    if request.user.is_authenticated:
        return render(request, 'notebook/html/indexforuser.html', {'user': request.user.username})
    else:
        return HttpResponseRedirect('/login/')


def user_login(request):
    if request.user.is_authenticated:
        return render(request, 'notebook/html/indexforuser.html', {'user': request.user.username})
    if request.method == "POST":

        fm = LoginForm(request=request, data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data.get('username')
            password = fm.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/user/')
        return render(request, 'notebook/html/login.html', {'form': fm})
    fm = LoginForm()
    return render(request, 'notebook/html/login.html', {'form': fm})


def user_logout(request):

    logout(request)

    return HttpResponseRedirect('/login/')
