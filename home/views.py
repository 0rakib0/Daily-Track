from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from transactions.models import TotalBalance, Express, Income
from django.db.models import Q, Sum
# Create your views here.

@login_required
def Dashbord(request):
    total_blance = TotalBalance.objects.get(user=request.user)
    expenses = Express.objects.filter(Q(user=request.user)).select_related('user')
    total_expense = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    income = Income.objects.filter(Q(user=request.user)).select_related('user')
    total_income = income.aggregate(Sum('amount'))['amount__sum'] or 0
    context = {
        'total_blance':total_blance,
        'total_expense':total_expense,
        'total_income':total_income,
    }
    
    return render(request, 'Home/dashbord.html', context)