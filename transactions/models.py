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
    depo_type = models.CharField(max_length=150)
    note = models.CharField(max_length=260)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    deposite_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.user.username
    
    
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
    send_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='send_user')
    receive_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receive_user')
    account_number = models.CharField(max_length=3600)
    amount = models.FloatField(default=0)
    note = models.TextField()
    transection_date = models.DateTimeField(auto_now_add=True)
    
class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    sourse = models.CharField(max_length=260)
    income_category = models.CharField(max_length=260)
    note = models.TextField()
    create_att = models.DateTimeField(auto_now_add=True)
    update_att = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.sourse


class Express(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    purpose = models.CharField(max_length=260)
    express_category = models.CharField(max_length=260)
    note = models.TextField()
    create_att = models.DateTimeField(auto_now_add=True)
    update_att = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.purpose
