from django.db import models
from django import forms
# Create your models here.


class Day(models.Model):
    date = models.DateField()
    one_sentence_description = models.CharField(max_length=200)
    today_i_learned = models.CharField("Today I learned",max_length=200)
    tags = models.CharField(max_length=200)
    content = models.TextField(max_length=10000)

    def __str__(self):
        return str(self.date) + ' | ' + str(self.one_sentence_description)


class Month(models.Model):
    date = models.DateField()
    one_sentence_description = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    content = models.TextField(max_length=10000)

    def __str__(self):
        return str(self.date) + ' | ' + str(self.one_sentence_description)


class Year(models.Model):
    year = models.PositiveIntegerField()
    one_sentence_description = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    content = models.TextField(max_length=10000)

    def __str__(self):
        return str(self.year) + ' | ' + str(self.one_sentence_description)


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)


class Chapter(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    attributes = models.TextField(max_length=1000, blank=True)
    content = models.TextField(max_length=100000, blank=True)

    def __str__(self):
        return str(self.name)


class List(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return str(self.name)


class ElementInList(models.Model):
    name = models.CharField(max_length=50)
    list = models.ForeignKey(List, on_delete=models.PROTECT)
    status = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=1000, blank=True)

    class Meta:
        verbose_name_plural = "List elements"

    def __str__(self):
        return str(self.name)