from django.shortcuts import render
from .models import Category, PomodoroSession, ToDoItem

# Create your views here.
def index(request):
    todos = ToDoItem.objects.order_by('category')
    context = {'todo': todos}
    return render(request, 'organizer/index.html', context)