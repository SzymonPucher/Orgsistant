from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Day
# Create your views here.
def index(request):
    days = Day.objects.all()
    context = {'days': days}
    return render(request, 'journal/index.html', context)
