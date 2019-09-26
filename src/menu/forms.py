from django import forms
from .models import Template

MENU_OPTIONS = [
    ('1.', 'one'),
    ('2.', 'snmp'),
    ('3.', 'anchoas')
]


class MenuForm(forms.Form):
    content = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=MENU_OPTIONS,
    )
