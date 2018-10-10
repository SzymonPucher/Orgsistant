from django.shortcuts import render
from .models import Recipe

# Create your views here.
def index(request):
    context = {}
    return render(request, 'nutrition/index.html', context)