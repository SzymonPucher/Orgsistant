from django.shortcuts import render
from .models import Category, PomodoroSession, ToDoItem

# Create your views here.
def index(request):
    todos = ToDoItem.objects.exclude(category__name='Codzienne')
    every_day = ToDoItem.objects.filter(category__name='Codzienne')
    context = {'todo': todos, 'ed': every_day}
    return render(request, 'organizer/index.html', context)