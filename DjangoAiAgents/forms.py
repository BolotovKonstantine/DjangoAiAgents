from django import forms

class PromptForm(forms.Form):
    prompt = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))