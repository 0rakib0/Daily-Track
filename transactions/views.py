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


def View_Banks(request):
    user = request.user
    banks = Bank.objects.filter(user=user)
    if not banks.exists():
        messages.warning(request, 'No Bank Found.')
    context = {
        'banks':banks
    }
    
    return render(request, 'transaction/view-banks.html', context)

def UpdateBank(request, id):
    bank_name = None
    bank_account_number = None
    if request.method == 'POST':
        bank_name = request.POST.get('bank-name')
        bank_account_number = request.POST.get('account-number')
        
        
    try:
        bank = Bank.objects.get(id=id)
        if bank_name and bank_account_number:
            bank.bank_name = bank_name
            bank.account_number = bank_account_number
            bank.save()
            messages.success(request, "Bank details successfully updated!")
            return redirect('transaction:view_bank')
    except Bank.DoesNotExist:
        messages.error(request, 'Bank Info not found, something wrong')
    return render(request, 'transaction/update-bank.html', context={'bank':bank})



def DeleteBank(requuest, id):
    try:
        bank = Bank.objects.get(id=id)
        bank.delete()
        messages.success(requuest, 'Bank details deletd!')
    except Bank.DoesNotExist:
        messages.error(requuest, 'Bank Info not found, something wrong')
        
    return redirect('transaction:view_bank')