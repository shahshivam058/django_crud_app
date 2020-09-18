from django import forms 
from .models import todo

class Todo_form(forms.ModelForm):

    class Meta:
        model = todo
        fields = ['name','due_date']