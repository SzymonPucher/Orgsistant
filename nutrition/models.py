from django.db import models
from budget.models import Product

# Create your models here.


class ProductNutritionValues(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    energy = models.DecimalField('Energy (cal)', max_digits=6, decimal_places=2, blank=True)
    protein = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    carbohydrate = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    sugars = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    fat = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    fibre = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    sodium = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    salt = models.DecimalField(max_digits=6, decimal_places=2, blank=True)

    class Meta:
        verbose_name_plural = "Product nutrition values"

    def __str__(self):
        return str(self.product)


class Recipe(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    image = models.ImageField()
    ingredients = models.TextField(max_length=10000)
    cooking_instructions = models.TextField(max_length=10000)

    def __str__(self):
        return self.name

