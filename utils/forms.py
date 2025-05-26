from django import forms
from .models import SheduleMail, Note, Tasks, FutureWork, Project, ProjectPlan

class ShedulemailForm(forms.ModelForm):
    class Meta:
        model = SheduleMail
        fields = ['mail_subject', 'message', 'sent_from', 'sent_to', 'shedule_date']
        widgets = {
            'mail_subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your message here', 'rows': 4}),
            'sent_from': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sender Email'}),
            'sent_to': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Recipient Email'}),
            'shedule_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'placeholder': 'Select date and time'
            }),

        }
        input_formats = {
            'shedule_date': ['%Y-%m-%dT%H:%M']
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
        
class FutureWorkForm(forms.ModelForm):
    class Meta:
        model = FutureWork
        fields = ['title', 'work_details', 'shedule_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'work_details': forms.Textarea(attrs={
                'class': 'form-control ckdesign', 
                'placeholder': 'Write work Details...', 
                'rows': 5,  # Adjust height
                'style': 'display: block; width: 100%;'
            }),
            'shedule_date':forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Select a date'}),
        }
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'project_details', 'what_problem_solvIt', 'project_status','project_live_link']
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter project name'}),
            'project_details': forms.Textarea(attrs={
                'class': 'form-control ckdesign', 
                'placeholder': 'Write project Details...', 
                'rows': 5,  # Adjust height
                'style': 'display: block; width: 100%;'
            }),
            'what_problem_solvIt': forms.Textarea(attrs={
                'class': 'form-control ckdesign', 
                'placeholder': 'whats type of problem solv this project ...', 
                'rows': 5,  # Adjust height
                'style': 'display: block; width: 100%;'
            }),
            'project_live_link': forms.Textarea(attrs={
                'class': 'form-control ckdesign', 
                'placeholder': 'Project ive link if complate...', 
                'rows': 5,  # Adjust height
                'style': 'display: block; width: 100%;'
            }),
        }
        
class ProjectPlanForm(forms.ModelForm):
    class Meta:
        model = ProjectPlan
        fields = ['project', 'date', 'topic_list']
        widgets = {
            'date':forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Select a date'}),
            'topic_list': forms.Textarea(attrs={
                'class': 'form-control ckdesign', 
                'placeholder': 'Write all topic list...', 
                'rows': 5,  # Adjust height
                'style': 'display: block; width: 100%;'
            }),
        }