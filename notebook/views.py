from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
import json
from .tests import querystrtoperm
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Notes
from django.contrib.auth.models import Group
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/user/')
    if request.method == "POST":
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            user = fm.save()
            group = Group.objects.get(name='normalusers')
            user.groups.add(group)
        # else:
        #     messages.error(request, "Registration Failed")
        return render(request, 'notebook/html/index.html', {'form': fm})
    fm = RegistrationForm()
    return render(request, 'notebook/html/index.html', {'form': fm})


def user_page(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            data = dict(request.POST)
            print(type(request.user.username))
            note = Notes(username=request.user.username,
                         title=data.get('title')[0],
                         desc=data.get('description')[0])
            print(note)
            note.save()
            # messages.success(request, "Note Added")
            return render(request, 'notebook/html/indexforuser.html',
                          {'user': request.user.username})
        return render(request, 'notebook/html/indexforuser.html',
                      {'user': request.user.username})
    else:
        return HttpResponseRedirect('/login/')


def user_login(request):
    if request.user.is_authenticated:
        return render(request, 'notebook/html/indexforuser.html',
                      {'user': request.user.username})
    if request.method == "POST":

        fm = LoginForm(request=request, data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data.get('username')
            password = fm.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/user/')
        messages.error(request, "Invalid Credentials")
        return HttpResponseRedirect('/login/')
    fm = LoginForm()
    return render(request, 'notebook/html/login.html', {'form': fm})


def user_notes(request):
    if request.user.is_authenticated:
        notes = list(Notes.objects.filter(username=request.user.username))
        notes = list(map(lambda a: str(a), notes))
        notes = list(
            map(lambda a: json.loads(a),
                notes))  # converting data(fetched from db ) to list of dict
        print(notes)
        return render(request, 'notebook/html/usernotes.html', {
            'user': request.user,
            'notes': notes
        })
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):

    logout(request)

    return HttpResponseRedirect('/login/')
