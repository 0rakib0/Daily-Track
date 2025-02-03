from django.contrib import admin
from .models import Bank, Account, TotalBalance, TransectionCategory, Transaction, Income, Express
# Register your models here.
admin.site.register(Bank)
admin.site.register(Account)
admin.site.register(TotalBalance)
admin.site.register(TransectionCategory)
admin.site.register(Transaction)
admin.site.register(Income)
admin.site.register(Express)