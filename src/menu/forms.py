from django import forms
from .models import Menu

MENU_OPTIONS = [
    ('1.', 'one'),
    ('2.', 'snmp'),
    ('3.', 'anchoas')
]


class MenuForm(forms.Form):
    templates = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=MENU_OPTIONS,
    )
