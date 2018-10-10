from django.contrib import admin

# Register your models here.
from .models import Recipe, ProductNutritionValues

admin.site.register(Recipe)
admin.site.register(ProductNutritionValues)