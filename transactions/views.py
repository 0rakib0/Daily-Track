from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Bank, Account, Income, Express, Transaction, TotalBalance
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
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

@login_required
def View_Banks(request):
    user = request.user
    banks = Bank.objects.filter(user=user)
    if not banks.exists():
        messages.warning(request, 'No Bank Found.')
    context = {
        'banks':banks
    }
    
    return render(request, 'transaction/view-banks.html', context)


@login_required
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



@login_required
def DeleteBank(requuest, id):
    try:
        bank = Bank.objects.get(id=id)
        bank.delete()
        messages.success(requuest, 'Bank details deletd!')
    except Bank.DoesNotExist:
        messages.error(requuest, 'Bank Info not found, something wrong')
        
    return redirect('transaction:view_bank')


@login_required
def deposit_blance(request):
    user = request.user
    try:
        banks = Bank.objects.filter(user=user)
        total_balance_obj = TotalBalance.objects.get(user=user)
    except Exception as e:
        messages.error(request, f"Your Balance deposit not success! Error: {e}")
        return redirect('transaction:transection_blance')
    if request.method == 'POST':
        bank_id = request.POST.get('bank')
        depo_type = request.POST.get('depo_type')
        note = request.POST.get('note')
        amount = request.POST.get('amount')
        flot_amount = float(amount)
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
                amount = flot_amount                
            )
            accounts.save()
            total_balance_obj.balance += flot_amount
            total_balance_obj.save()
            messages.success(request, 'Deposite amount successfully aded!')
            return redirect('transaction:deposit_blance')
        except IntegrityError:
            messages.warning(request, 'Error: Unable to added amount, please try again!')
        
    return render(request, 'transaction/deposit_blance.html', context={'banks':banks})


@login_required
def TotalBlance(request):
    total_plance = TotalBalance.objects.get(user=request.user)
    account_number = request.user.user_profile.account_number
    receiver_transection_data = Transaction.objects.filter(Q(receive_user=request.user) & Q(account_number=account_number))
    return render(request, 'transaction/total_plance.html', context={'total_plance':total_plance, 'receiver_transection_data':receiver_transection_data})

@login_required
def transection_blance(request):
    send_user = request.user
    user = request.user
    try:
        sender_total_balance = TotalBalance.objects.get(user=user)
    except TotalBalance.DoesNotExist:
        messages.error(request, "Your transaction does not complate. pleae tray again!")
        return redirect('transaction:transection_blance')
    
    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        username = request.POST.get('username')
        amount = request.POST.get('amount')
        float_amount = float(amount)
        note = request.POST.get('note')
        
        try:
            receive_user = User.objects.get(username=username)
            receiver_total_balance = TotalBalance.objects.get(user=receive_user)
        except Exception as e:
            messages.error(request, f"Your transaction does not complate. pleae tray again. error: {e}")
            return redirect('transaction:transection_blance')
        
        sender_total = sender_total_balance.balance
        
        if sender_total < float_amount:
            messages.error(request, f'You have not available blance. Your balance is {sender_total} tk')
            return redirect('transaction:transection_blance')
        else:
            transection = Transaction(
                send_user = send_user,
                receive_user = receive_user,
                account_number = account_number,
                amount = float_amount,
                note = note
            )
            transection.save()
            sender_total_balance.balance -= float_amount
            sender_total_balance.save()
            
            receiver_total_balance.balance += float_amount
            receiver_total_balance.save()
            
            messages.success(request, 'Transection successfully complated!')
            return redirect('transaction:transection_blance')
        
    return render(request, 'transaction/transection.html', context={})



@login_required
def transection_data(request):
    current_user = request.user
    transection_data = Transaction.objects.filter(send_user=current_user)
    if not transection_data.exists():
        messages.warning(request, "No Transection Data Available.")
    context = {
        'transection_data':transection_data
    }
    return render(request, 'transaction/transection_data.html', context)


@login_required
def receive_transection(request):
    current_user = request.user
    account_number = request.user.user_profile.account_number
    receiver_transection_data = Transaction.objects.filter(Q(receive_user=current_user) & Q(account_number=account_number))
    
    if not receiver_transection_data.exists():
        messages.warning(request, "No Transection Data Available.")
    context = {
        'receive_transection':receiver_transection_data
    }
    return render(request, 'transaction/receive_transection.html', context)



@login_required
def Add_Income(request):
    if request.method == 'POST':
        total_blance = TotalBalance.objects.get(user=request.user)
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
            total_blance.balance += float(amount)
            total_blance.save()
            messages.success(request, "Income successfully Added!")
            return redirect('transaction:add_income')
        except IntegrityError:
            messages.warning(request, 'Error: Unable to added bank account, please try again!')
            return redirect('transaction:add_income')
        except Exception as e:
            messages.error(request, 'Somethink wrong, ', e)
            return redirect('transaction:add_income')
    return render(request, 'transaction/add_inome.html', context={})


@login_required
def View_Income(request):
    user = request.user
    income_data = Income.objects.filter(user=user)
    print(income_data)
    return render(request, 'transaction/view_income.html', context={'income_data':income_data})


@login_required
def UpdateIncome(request, id):
    user = request.user
    try:
       income_data = Income.objects.get(user=user, id=id)
    except Income.DoesNotExist:
        messages.error(request, 'Data Not Found, Please Try Again!')
        return redirect("transaction:view_income")
    if request.method == "POST":
        amount = request.POST.get('amount')
        income_source = request.POST.get('income_source')
        income_category = request.POST.get('income_category')
        note = request.POST.get('note')
        
        income_data.amount = amount
        income_data.sourse = income_source
        income_data.income_category = income_category
        income_data.note = note
        income_data.save()
        messages.success(request, "Income Data successfully updated")
        return redirect("transaction:view_income")
    return render(request, 'transaction/update_income.html', context={'income_data':income_data})


@login_required
def DeleteIncome(request, id):
    user = request.user
    try:
        income_data = Income.objects.get(user=user, id=id)
        income_data.delete()
        messages.success(request, "Income Data Successfully Deleted!")
        return redirect("transaction:view_income")
    except Income.DoesNotExist:
        messages.error(request, "Data Not Found, Try Again")
        return redirect("transaction:view_income")
    

@login_required
def Add_Express(request):
    if request.method == 'POST':
        total_blance = TotalBalance.objects.get(user=request.user)
        amount = request.POST.get('amount')
        purpose = request.POST.get('purpose')
        express_category = request.POST.get('express_category')
        note = request.POST.get('note')
        
        if total_blance.balance < int(amount):
            messages.error(request, "You do not have anought amount for expense")
            return redirect('transaction:add_express')
        
        try:
            express = Express.objects.create(
                user = request.user,
                amount = amount,
                purpose = purpose,
                express_category = express_category,
                note = note
            )
            express.save()
            total_blance.balance -= float(amount)
            total_blance.save()
            messages.success(request, "Express successfully Added!")
            return redirect('transaction:add_express')
        except IntegrityError:
            messages.warning(request, 'Error: Unable to added bank account, please try again!')
            return redirect('transaction:add_express')
        except Exception as e:
            messages.error(request, 'Somethink wrong, ', e)
            return redirect('transaction:add_express')
    return render(request, 'transaction/add_express.html', context={})


@login_required
def View_Express(request):
    user = request.user 
    expreses = Express.objects.filter(user=user)
    return render(request, 'transaction/view_express.html', context={'expreses':expreses})


@login_required
def UpdateExpress(request, id):
    user = request.user
    try:
       express_data = Express.objects.get(user=user, id=id)
    except Express.DoesNotExist:
        messages.error(request, 'Data Not Found, Please Try Again!')
        return redirect("transaction:view_express")
    if request.method == "POST":
        amount = request.POST.get('amount')
        purpose = request.POST.get('purpose')
        express_category = request.POST.get('express_category')
        note = request.POST.get('note')
        
        express_data.amount = amount
        express_data.purpose = purpose
        express_data.express_category = express_category
        express_data.note = note
        express_data.save()
        messages.success(request, "Express Data successfully updated")
        return redirect("transaction:view_express")
    return render(request, 'transaction/update_express.html', context={'express_data':express_data})


@login_required
def DeleteExpress(request, id):
    user = request.user
    try:
        expess_data = Express.objects.get(user=user, id=id)
        expess_data.delete()
        messages.success(request, "Express Data Successfully Deleted!")
        return redirect("transaction:view_express")
    except Express.DoesNotExist:
        messages.error(request, "Data Not Found, Try Again")
        return redirect("transaction:view_express")
    
