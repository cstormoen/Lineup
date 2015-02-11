from django.forms import ModelForm, TextInput, NumberInput
from lineup.models import Lineup, Entry


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['rank', 'text']
        labels = {
            'rank': '',
            'text': '',
            'delete': '',
        }
        widgets = {
            'rank': NumberInput(attrs={'size': 2}),
            'text': TextInput(attrs={'size': 30})
        }


class LineupForm(ModelForm):
    class Meta:
        model = Lineup
        fields = ['title']
        widgets = {
            'title': TextInput(attrs={'size': 30})
        }