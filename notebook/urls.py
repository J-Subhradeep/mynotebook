from django.urls import path
from .views import home, user_login

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='user_login'),
]