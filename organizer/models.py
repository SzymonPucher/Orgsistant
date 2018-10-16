from django.db import models

# Create your models here.


class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])


class ToDoItem(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    due = models.DateField(null=True, blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        if self.done:
            return 'Done | ' + str(self.category) + ' | ' + self.name
        return str(self.category) + ' | ' + self.name

    def change_status(self):
        if self.done:
            self.done = False
        else:
            self.done = True


class PomodoroSession(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    date = models.DateField()
    duration = models.DurationField()

    def __str__(self):
        return str(self.duration.seconds // 60 % 60) + ' min | ' + str(self.date) + ' | ' + str(self.category)
