from django.forms import ModelForm
from . import models

# this is just an example
class UserForm(forms.ModelForm):
    pass
    
class GoalsForm(forms.ModelForm):

    class Meta:
        model = models.Goals
        fields = ['goal']
