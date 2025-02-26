from django import forms
from .models import SheduleMail

class ShedulemailForm(forms.ModelForm):
    class Meta:
        model = SheduleMail
        fields = ['mail_subject', 'message', 'sent_from', 'sent_to', 'shedule_date']
        widgets = {
            'shedule_date': forms.DateInput(attrs={'type': 'date'})  # This will render a date input field
        }