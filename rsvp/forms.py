# forms.py
from django import forms

class RSVPForm(forms.Form):
    name = forms.CharField(max_length=200)
    num_attendees = forms.IntegerField(initial=1, min_value=1, widget=forms.NumberInput(attrs={'auto_id': 'id_num_attendees'}))


