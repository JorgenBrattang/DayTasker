from django.db import models
from datetime import timedelta, date


class Task(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    status_choice = (
        ('not_done', 'Not Done'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    )
    status = models.CharField(
        max_length=50, default='not_done', choices=status_choice)
    date = models.DateTimeField(auto_now=True)
    estimated = models.PositiveIntegerField(null=True, blank=True)
    last_done = models.DateField(null=True, blank=True)
    repeat_task = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, id=0):
        if self.id is not None:
            get_task = Task.objects.get(pk=self.id)
            old_estimated_value = get_task.estimated
            if self.status == 'done':
                self.last_done = self.date + timedelta(days=self.repeat_task)
            print(self.last_done)
            print(date.today())
            if self.last_done == date.today():
                print('success')
            else:
                print('Its not today..')
            if old_estimated_value is not None:
                new_estimated_value = self.estimated
                estimated = (old_estimated_value + new_estimated_value) / 2
                self.estimated = estimated
        super(Task, self).save(force_insert, force_update)
