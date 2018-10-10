from django.contrib import admin

# Register your models here.
from .models import Category, PomodoroSession, ToDoItem

admin.site.register(Category)
admin.site.register(PomodoroSession)
admin.site.register(ToDoItem)
