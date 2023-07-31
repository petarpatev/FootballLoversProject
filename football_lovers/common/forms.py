from django import forms

from football_lovers.common.models import Story


class StoryUpdateForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = ('title', 'content')