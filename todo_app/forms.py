from django import forms
from .models import todoform

class TaskForm(forms.ModelForm):
    class Meta:
        model = todoform
        fields="__all__"

#class TaskForm(forms.ModelForm):
#	title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
#	desc = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'enter description...'}))
#	class Meta:
#		model = todoform
#		fields = ['title' ,'desc']