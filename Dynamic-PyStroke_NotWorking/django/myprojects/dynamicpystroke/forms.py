from django import forms
from .models import UserDatas
from django.forms import ModelForm

class HomeForm(forms.ModelForm):
    class Meta:
        model = UserDatas
        fields = ('Email1','Password1',)
