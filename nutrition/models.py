from django.db import models
from budget.models import Currency
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ('name',)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=128, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = models.ImageField(blank=True, null=True)
    cooking_time = models.DurationField()
    estimated_price_pln = models.DecimalField(max_digits=5, decimal_places=2)
    ingredients = models.TextField(max_length=2000)
    cooking_instructions = models.TextField(max_length=10000)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

