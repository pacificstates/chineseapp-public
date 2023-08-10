from django import forms
from .models import CustomCards

class CreateNewCard(forms.ModelForm):
    class Meta:
        model = CustomCards
        fields = ['chinese', 'pinyin', 'english']

