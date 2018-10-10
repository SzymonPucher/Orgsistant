from django.contrib import admin

# Register your models here.
from .models import Recipe, Category

admin.site.register(Recipe)
admin.site.register(Category)
