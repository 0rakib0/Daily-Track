from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from transactions.models import TotalBalance, Express, Income, Transaction
from django.db.models import Q, Sum
# Create your views here.

@login_required
def Dashbord(request):
    total_blance = TotalBalance.objects.get(user=request.user)
    
    expenses = Express.objects.filter(Q(user=request.user)).select_related('user')
    recent_expenses = expenses.order_by('-id')[:5]
    total_expense = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    
    income = Income.objects.filter(Q(user=request.user)).select_related('user')
    recent_income = income.order_by('-id')[:5]
    total_income = income.aggregate(Sum('amount'))['amount__sum'] or 0
    
    account_number = request.user.user_profile.account_number
    receiver_transection_data = Transaction.objects.filter(Q(receive_user=request.user) & Q(account_number=account_number))
    print(receiver_transection_data)
    recent_receive_transection = receiver_transection_data.order_by('-id')[:5]
    context = {
        'total_blance':total_blance,
        'total_expense':total_expense,
        'total_income':total_income,
        'recent_expenses':recent_expenses,
        'recent_income':recent_income,
        'recent_receive_transection':recent_receive_transection
    }
    
    return render(request, 'Home/dashbord.html', context)