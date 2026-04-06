from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

class SearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False)


