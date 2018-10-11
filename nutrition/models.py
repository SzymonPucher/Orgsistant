from django.db import models
from budget.models import Currency
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=1000, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=128, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = models.ImageField(blank=True, null=True)
    cooking_time = models.DurationField()
    estimated_price = models.DecimalField(max_digits=5, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, default=1)
    ingredients = models.TextField(max_length=2000)
    cooking_instructions = models.TextField(max_length=10000)

    def __str__(self):
        return self.name

