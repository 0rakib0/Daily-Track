from django.contrib import admin
from .models import Bank, Account, TotalAmount, TransectionCategory, Transaction, Income, Express
# Register your models here.
admin.site.register(Bank)
admin.site.register(Account)
admin.site.register(TotalAmount)
admin.site.register(TransectionCategory)
admin.site.register(Transaction)
admin.site.register(Income)
admin.site.register(Express)