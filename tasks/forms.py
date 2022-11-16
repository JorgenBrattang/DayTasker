from django import forms
from .models import Task


class AddTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'status', 'estimated',)
        labels = {
            'name': 'What do you want to add? ',
            'status': 'What is the status of the task?',
            'estimated': 'Estimated time to complete? (optional)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
