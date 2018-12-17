from django.db import models
from django import forms
# Create your models here.


class Mood(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(max_length=1024, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)


class Day(models.Model):
    date = models.DateField(unique=True)
    mood = models.ForeignKey(Mood, on_delete=models.PROTECT)
    important_thing_that_happened = models.TextField(max_length=256, blank=True)
    one_sentence_description = models.TextField(max_length=256)
    today_i_learned = models.TextField("Today I learned", max_length=256, blank=True)
    food_eaten = models.TextField(max_length=512, blank=True)
    tags = models.TextField(max_length=256, blank=True)
    content = models.TextField(max_length=10000)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return str(self.date) + ' | ' + str(self.one_sentence_description)


class Month(models.Model):
    date = models.DateField(unique=True)
    one_sentence_description = models.CharField(max_length=256)
    accomplishments = models.TextField(max_length=2048)
    tags = models.CharField(max_length=256, blank=True)
    content = models.TextField(max_length=10000)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return str(self.date.year) + '-' + str(self.date.month) + ' | ' + str(self.one_sentence_description)


class Year(models.Model):
    year = models.PositiveIntegerField(unique=True)
    one_sentence_description = models.CharField(max_length=256)
    accomplishments = models.TextField(max_length=2048)
    tags = models.CharField(max_length=256, blank=True)
    portrait = models.ImageField(blank=True, null=True)
    content = models.TextField(max_length=10000)

    class Meta:
        ordering = ('-year',)

    def __str__(self):
        return str(self.year) + ' | ' + str(self.one_sentence_description)


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ('name',)

    def __str__(self):
        return str(self.name)


class Chapter(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    attributes = models.TextField(max_length=1024, blank=True)
    content = models.TextField(max_length=100000)

    class Meta:
        ordering = ('category__name', 'name')

    def __str__(self):
        return str(self.category) + ' | ' + str(self.name)


class List(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(max_length=1024, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return str(self.name)


class ElementInList(models.Model):
    name = models.CharField(max_length=64)
    list = models.ForeignKey(List, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "List elements"
        ordering = ('list__name', 'name')

    def __str__(self):
        return str(self.list) + ' | ' + str(self.name)
