from django.db import models
import datetime
# Create your models here.

# TODO: Streak for 'Codzienne'

class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ('name',)

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' <- '.join(full_path[::1])


class ToDoItem(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    due = models.DateField(null=True, blank=True)
    done = models.BooleanField(default=False)

    class Meta:
        ordering = ('done', 'category__name', 'name')

    def __str__(self):
        if self.done:
            return 'Done | ' + str(self.category) + ' | ' + self.name
        return str(self.category) + ' | ' + self.name

    def change_status(self):
        if self.done:
            self.done = False
            if self.category.name == 'Codzienne':
                self.due = None
        else:
            self.done = True
            if self.category.name == 'Codzienne':
                self.due = datetime.datetime.today()
        self.save()

    def how_soon(self):
        if self.due is not None:
            for i in range(3):
                if self.due - datetime.datetime.today().date() == datetime.timedelta(i):
                    return 'soon' + str(i)
            return 'is_due'

    def streak_up(self):
        if len(self.name.split(' | Streak: ')) == 1:
            self.name = self.name + ' | Streak: 1'
        else:
            self.name = self.get_name() + ' | Streak: ' + str(self.get_streak() + 1)
        self.save()

    def streak_reset(self):
        self.name = self.name.split(' | ')[0]
        self.save()

    def get_name(self):
        return self.name.split(' | ')[0]

    def get_streak(self):
        if len(self.name.split(' | Streak: ')) > 1:
            return int(self.name.split(' | Streak: ')[1])
        return 0


class PomodoroSession(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    date = models.DateField()
    duration = models.DurationField()

    class Meta:
        ordering = ('-date', 'category__name')

    def __str__(self):
        return str(self.duration.seconds // 60 % 60) + ' min | ' + str(self.date) + ' | ' + str(self.category)
