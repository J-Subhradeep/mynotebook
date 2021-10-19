from django.contrib import admin
from .models import Notes


# Register your models here.
@admin.register(Notes)
class AdminNote(admin.ModelAdmin):
    list_display = ('id', 'username', 'title', 'desc')
