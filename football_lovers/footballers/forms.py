from django import forms

from football_lovers.footballers.models import Footballer


class FootballerUpdateForm(forms.ModelForm):
    class Meta:
        model = Footballer
        exclude = ('user',)
