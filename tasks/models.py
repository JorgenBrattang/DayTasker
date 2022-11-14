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

    def __str__(self):
        return self.name
