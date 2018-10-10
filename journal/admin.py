from django.contrib import admin

# Register your models here.
from .models import Mood, Day, Month, Year, Category, Chapter, List, ElementInList

admin.site.register(Mood)
admin.site.register(Day)
admin.site.register(Month)
admin.site.register(Year)
admin.site.register(Category)
admin.site.register(Chapter)
admin.site.register(List)
admin.site.register(ElementInList)




