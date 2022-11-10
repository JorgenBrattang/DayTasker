from django import forms
from .models import Task


class AddTask(forms.ModelForm):

    class Meta:
        model = Task
        # fields = '__all__'  <<< --- This will show in the order of creation
        fields = ('name', 'done')
        labels = {
            'name': 'What do you want to add? ',
            'done': 'Is the task done already? '
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
