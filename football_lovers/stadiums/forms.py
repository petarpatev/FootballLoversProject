from django import forms

from football_lovers.stadiums.models import Stadium


class StadiumUpdateForm(forms.ModelForm):
    class Meta:
        model = Stadium
        exclude = ('user',)
