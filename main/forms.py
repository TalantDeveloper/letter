from django import forms
from .models import Letter


class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ['control_card', 'group', 'reporter', 'document_type', 'registration_date', 'registration_number', 'document_number', 'document_date', 'summary', 'resolution', 'auth_resolution', 'type_solution']
