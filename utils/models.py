from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField  # Make sure to import it from ckeditor.fields
# Create your models here.


class BudgetCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat_name = models.CharField(max_length=160)
    create_at = models.DateTimeField(auto_now_add=True) 


    def __str__(self):
        return self.cat_name

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="budget")
    title = models.CharField(max_length=255)
    category = models.ForeignKey(BudgetCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    
class SheduleMail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mail_subject = models.CharField(max_length=360)
    message = models.TextField()
    sent_from = models.EmailField(max_length=254, blank=False, null=False)
    sent_to = models.EmailField(max_length=254, blank=False, null=False)
    is_sent = models.BooleanField(default=False)
    shedule_date = models.DateTimeField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.user.username} | {self.mail_subject}"

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_task')
    task_title = models.CharField(max_length=266)
    task_details = RichTextField()
    is_complated = models.BooleanField(default=False)
    create_att = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.task_title
    
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note_title = models.CharField(max_length=266)
    note = RichTextField()
    
    def __str__(self):
        return self.note_title
    
class FutureWork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_future_work')
    title = models.CharField(max_length=266)
    work_details = RichTextField()
    shedule_date = models.DateField()
    is_done = models.BooleanField(default=False)
    create_att = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=166)
    project_details = RichTextField()
    what_problem_solvIt = models.TextField()
    project_status = models.BooleanField(default=False)
    project_duration = models.IntegerField(default=1)
    project_live_link = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.project_name
    
class ProjectPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_plan')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateField()
    topic_list =RichTextField()
    status = models.BooleanField(default=False)
    create_att = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.project.project_name