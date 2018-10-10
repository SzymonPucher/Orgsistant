from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class ToDoItem(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    due = models.DateField(null=True, blank=True)
    reps = (
        ('no', 'Never'),
        ('day', 'Every day'),
        ('week', 'Every week'),
        ('month', 'Every month'),
        ('year', 'Every year')
    )
    repetition = models.CharField(max_length=5, choices=reps, default='no')


    def __str__(self):
        return self.name

class PomodoroSession(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    date = models.DateField(null=True, blank=True)
    duration = models.DurationField()

    def __str__(self):
        return str(self.date) + ' | ' + str(self.duration) + ' | ' + str(self.category)
