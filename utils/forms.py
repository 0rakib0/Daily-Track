from django import forms
from .models import SheduleMail, Note, Tasks

class ShedulemailForm(forms.ModelForm):
    class Meta:
        model = SheduleMail
        fields = ['mail_subject', 'message', 'sent_from', 'sent_to', 'shedule_date']
        widgets = {
            'mail_subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your message here', 'rows': 4}),
            'sent_from': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sender Email'}),
            'sent_to': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Recipient Email'}),
            'shedule_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Select a date'}),
        }
        
        
        
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note_title', 'note']
        labels = {
            'note': 'Importent Note  Content',  # Custom label
        }
        widgets = {
            'note_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter note title'}),
            'note': forms.Textarea(attrs={
                'class': 'form-control ckdesign', 
                'placeholder': 'Write your note here...', 
                'rows': 5,  # Adjust height
                'style': 'display: block; width: 100%;'
            }),
        }


class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['task_title', 'task_details', 'is_complated']
        widgets = {
            'task_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Tasks title'}),
            'task_details': forms.Textarea(attrs={
                'class': 'form-control ckdesign', 
                'placeholder': 'Write Tasks Details here...', 
                'rows': 5,  # Adjust height
                'style': 'display: block; width: 100%;'
            }),
        }