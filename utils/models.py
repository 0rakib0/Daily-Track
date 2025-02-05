from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BudgetCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat_name = models.CharField(max_length=160)
    create_at = models.DateTimeField(auto_now_add=True) 


    def __str__(self):
        return self.cat_name

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(BudgetCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    
    