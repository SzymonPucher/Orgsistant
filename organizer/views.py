from django.shortcuts import render, get_object_or_404
from .models import Category, PomodoroSession, ToDoItem
import datetime


# Create your views here.
def index(request, id=-1):
    try:
        item = get_object_or_404(ToDoItem, pk=id)  # get ToDoItem with given id
        item.change_status()
    except:
        print('')
    todos_done = ToDoItem.objects.exclude(category__name='Codzienne').exclude(done=False)
    todos = ToDoItem.objects.exclude(category__name='Codzienne').exclude(done=True)
    every_day_done = ToDoItem.objects.filter(category__name='Codzienne')
    for item in every_day_done:
        if item.due is not None and item.due < datetime.datetime.today().date() and item.done is True:
            item.done = False
            item.streak_up()
            item.save()
        else:
            item.streak_reset()
    context = {'todo': todos, 'ed': every_day_done, 'todo_done': todos_done}
    return render(request, 'organizer/index.html', context)
