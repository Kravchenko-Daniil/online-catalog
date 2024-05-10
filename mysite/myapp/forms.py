# # forms.py

from django import forms


class FilterForm(forms.Form):
    CHOICES = (
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    )
    dropdown = forms.MultipleChoiceField(choices=CHOICES, widget=forms.SelectMultiple, required=False)

    # checkbox1 = forms.BooleanField(required=False)
    # checkbox2 = forms.BooleanField(required=False)
