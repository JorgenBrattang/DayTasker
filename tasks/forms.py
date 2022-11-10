from django import forms
from .models import Task


class AddTask(forms.ModelForm):

    class Meta:
        model = Task
        # fields = '__all__'  <<< --- This will show in the order of creation
        fields = ('name', 'done')
