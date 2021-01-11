from django import forms
from django.forms import fields
from .models import Thought


MAX_THOUGHT_LENGTH = 240

class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > MAX_THOUGHT_LENGTH:
            raise forms.ValidationError('This thought is to long.')
        return content
