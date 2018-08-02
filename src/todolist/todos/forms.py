from django import forms
from datetime import *



class Todo_Form(forms.Form):
    task_title = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control',
                                'id':'task_title','placeholder':'Enter Title'}))
    task_description = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control',
                                        'id': 'task_desc','placeholder': 'Describe the task'}))
