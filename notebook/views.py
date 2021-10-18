from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def home(request):
    if request.method == "POST":
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
        # else:
        #     messages.error(request, "Registration Failed")
        return render(request, 'notebook/html/index.html', {'form': fm})
    fm = RegistrationForm()
    return render(request, 'notebook/html/index.html', {'form': fm})


def user_login(request):
    if request.method == "POST":

        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data.get('username')
            password = fm.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
        return render(request, 'notebook/html/login.html', {'form': fm})
    fm = AuthenticationForm()
    return render(request, 'notebook/html/login.html', {'form': fm})