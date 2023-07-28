from django import forms

from football_lovers.teams.models import Team


class TeamUpdateForm(forms.ModelForm):
    class Meta:
        model = Team
        exclude = ('user',)