from django.forms import ModelForm
from . import models

# this is just an example
class UserForm(forms.ModelForm):
    pass
    
class MissionForm(forms.ModelForm):
    class Meta:
        model = models.Mission
        fields = ['goal']
