from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Bank, Account, Income, Express
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


def deposit_blance(request):
    user = request.user
    banks = Bank.objects.filter(user=user)
    if request.method == 'POST':
        bank_id = request.POST.get('bank')
        depo_type = request.POST.get('depo_type')
        note = request.POST.get('note')
        amount = request.POST.get('amount')
        try:
            bank = Bank.objects.get(id=bank_id)
        except Bank.DoesNotExist:
            print("Bank account not found, train again")
        
        try:
            accounts = Account(
                user = request.user,
                bank = bank,
                depo_type = depo_type,
                note = note,
                amount = amount                
            )
            accounts.save()
            messages.success(request, 'Deposite amount successfully aded!')
            return redirect('transaction:deposit_blance')
        except IntegrityError:
            messages.warning(request, 'Error: Unable to added amount, please try again!')
        
    return render(request, 'transaction/deposit_blance.html', context={'banks':banks})



def transection_blance(request):
    return render(request, 'transaction/transection.html', context={})


def Add_Income(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        income_source = request.POST.get('income_source')
        income_category = request.POST.get('income_category')
        note = request.POST.get('note')
        try:
            income = Income.objects.create(
                user = request.user,
                amount = amount,
                sourse = income_source,
                income_category = income_category,
                note = note
            )
            income.save()
            messages.success(request, "Income successfully Added!")
            return redirect('transaction:add_income')
        except IntegrityError:
            messages.warning(request, 'Error: Unable to added bank account, please try again!')
            return redirect('transaction:add_income')
        except Exception as e:
            messages.error(request, 'Somethink wrong, ', e)
            return redirect('transaction:add_income')
    return render(request, 'transaction/add_inome.html', context={})


def View_Income(request):
    return render(request, 'transaction/view_income.html', context={})

def Add_Express(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        purpose = request.POST.get('purpose')
        express_category = request.POST.get('express_category')
        note = request.POST.get('note')
        try:
            express = Express.objects.create(
                user = request.user,
                amount = amount,
                purpose = purpose,
                express_category = express_category,
                note = note
            )
            express.save()
            messages.success(request, "Express successfully Added!")
            return redirect('transaction:add_express')
        except IntegrityError:
            messages.warning(request, 'Error: Unable to added bank account, please try again!')
            return redirect('transaction:add_express')
        except Exception as e:
            messages.error(request, 'Somethink wrong, ', e)
            return redirect('transaction:add_express')
    return render(request, 'transaction/add_express.html', context={})


def View_Express(request):
    return render(request, 'transaction/view_express.html', context={})