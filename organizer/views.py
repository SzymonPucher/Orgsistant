from django.shortcuts import render
from .models import Category, PomodoroSession, ToDoItem

# Create your views here.
def index(request):
    context = {}
    return render(request, 'organizer/index.html', context)