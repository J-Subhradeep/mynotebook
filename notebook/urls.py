from django.urls import path
from .views import home, user_login, user_logout, user_page, user_notes, delete_notes, edit_note

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('user/', user_page, name='userpage'),
    path('notes/', user_notes, name='notes'),
    path('deletenotes/<int:id>/', delete_notes, name='deletenotes'),
    path('editnotes/<int:id>/', edit_note, name='editnotes'),
]
