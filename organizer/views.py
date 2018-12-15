from django.shortcuts import render, get_object_or_404
from .models import Category, PomodoroSession, ToDoItem
import datetime


# Create your views here.
def index(request, id=-1):
    if(id >= 0):
        item = get_object_or_404(ToDoItem, pk=id)  # get ToDoItem with given id
        item.change_status()
    todos_done = ToDoItem.objects.exclude(category__name='Codzienne').exclude(done=False)
    todos = ToDoItem.objects.exclude(category__name='Codzienne').exclude(done=True)
    every_day_done = ToDoItem.objects.filter(category__name='Codzienne')
    for item in every_day_done:
        if item.due < datetime.datetime.today().date() and item.done is True:
            item.done = False
            item.streak_up()

        elif item.due < datetime.datetime.today().date() and item.done is False:
            item.streak_reset()
        item.due = datetime.datetime.today()
        item.save()

    pomodoros = PomodoroSession.objects.all()
    print(pomodoros)
    pomos = []
    for p in pomodoros:
        x = True
        for p_temp in pomos:
            if p_temp[0] == str(p.date):
                p_temp[1] += 1
                x = False
        if x:
            pomos.append([str(p.date), 1])
    print(pomos)

    cats = Category.objects.all()
    p = PomodoroSession.objects.all()
    context = {'p': p, 'cats': cats,'todo': todos, 'ed': every_day_done, 'todo_done': todos_done, 'pomodoros': pomos}
    return render(request, 'organizer/index.html', context)
