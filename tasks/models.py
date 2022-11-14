from django.db import models
import datetime


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

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False):
        print('save')
        task = Task.objects.get(pk=self.id)
        old_estimated_value = task.estimated
        new_estimated_value = self.estimated
        estimated = (old_estimated_value + new_estimated_value) / 2
        self.estimated = estimated
        super(Task, self).save(force_insert, force_update)
