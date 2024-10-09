from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Bank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=120)
    account_number = models.CharField(max_length=160)
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.bank_name
    
    
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self) -> str:
        return self.bank
    
    
class TotalAmount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self) -> str:
        return f"{self.user.username} : {self.balance}"
    

class TransectionCategory(models.Model):
    category_name = models.CharField(max_length=160)
    
    def __str__(self) -> str:
        return self.category_name
    
    
class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    )
    category = models.ForeignKey(TransectionCategory, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"
