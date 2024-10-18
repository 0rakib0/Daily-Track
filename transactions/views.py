from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Bank
from django.db import IntegrityError
# Create your views here.

def AddBank(request):
    if request.method == 'POST':
        bank_name = request.POST.get('bank-name')
        bank_account_number = request.POST.get('account-number')

        try:
            bank = Bank(bank_name=bank_name, account_number=bank_account_number)
            bank.user = request.user
            bank.save()
            messages.success(request, 'Bank Account successfully Add!')
            return redirect('transaction:add_bank')
        except IntegrityError:
            messages.warning(request, 'Error: Unable to added bank account, please try again!')
        except Exception as e:
            messages.warning(request, f'An unexpected error occurred: {e}')
            
    return render(request, 'transaction/add-bank.html', context={})
