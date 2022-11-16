from django import forms
from .models import Category


class AddCategories(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
