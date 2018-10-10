from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64, primary_key=True)
    description = models.TextField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class ToDoItem(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    due = models.DateField(null=True, blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PomodoroSession(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    date = models.DateField(null=True, blank=True)
    duration = models.DurationField()

    def __str__(self):
        return str(self.date) + ' | ' + str(self.duration.minutes) + ' | ' + str(self.category)
