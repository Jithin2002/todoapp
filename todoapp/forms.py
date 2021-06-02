from django import forms
from todoapp.models import Todos
class TodoCreateForm(forms.Form):
    task_name=forms.CharField()
    user=forms.CharField()
    options=(("completed","completed"),("not completed","notcompleted"))
    status=forms.ChoiceField(choices=options)
#modelform
#update,static files
class TodoModelform(forms.ModelForm):
    model=Todos
    fields=["task_name","user","status"]
