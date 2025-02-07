from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Q

from .models import BudgetCategory, Budget
# Create your views here.


def add_budget_cat(request):
    try:
        user = request.user
    except Exception as e:
        messages.error(request, f"User  Does not matching.error: {e}")
    if request.method == "POST":
        cat_name = request.POST.get('cat_name')
        
        
        try:
            add_category = BudgetCategory(
                user = user,
                cat_name = cat_name
            )
            
            add_category.save()
            messages.success(request, "Budget Category successfully added!")
            return redirect('utils:add_budget_cat')        
        except IntegrityError:
             messages.warning(request, 'Error: Unable to added budget category, please try again!')
             return redirect('utils:add_budget_cat') 
        
        
        
    return render (request, 'utils/budget_cat_add.html', context={})
    
    

def view_budget_category(request):
    user = request.user
    try:
        budget_categorys = BudgetCategory.objects.filter(user = user)
    except Exception as e:
        messages.warning(request, F"Something wrong!Error:{e}")
        return redirect('utils:add_budget_cat')
    return render(request, 'utils/budget_cat.html', context={"categorys":budget_categorys})


def add_badget(request):
    user = request.user
    try:
        budget_categorys = BudgetCategory.objects.filter(user = user)
    except Exception as e:
        messages.warning(request, F"Something wrong!Error:{e}")
        return redirect('utils:add_budget')
    
    if request.method == "POST":
        budget_title = request.POST.get('budget-title')
        category_id = request.POST.get('category')
        budget_amount = request.POST.get('budget-amount')
        due_date = request.POST.get('budget-due-date')
        
        try:
            category_instance = BudgetCategory.objects.get(id=category_id)
        except BudgetCategory.DoesNotExist:
            messages.warning(request, 'Budget not added, something wrong!')
            return redirect('utils:add_budget')
        
        try:
            budget = Budget(
                user = user,
                title=budget_title,
                category = category_instance,
                amount = budget_amount,
                due_date = due_date
            )
            
            budget.save()
            messages.success(request, "Budget successfully added!")
            return redirect('utils:add_budget')
            
        except IntegrityError:
            messages.warning(request, 'Budget not added, something wrong!')
            return redirect('utils:add_budget')

    return render(request, 'utils/add_budget.html', context={'categorys':budget_categorys})


def view_budget(request):
    user = request.user
    
    try:
        budgets = Budget.objects.filter(user=user)
    except Exception as e:
        messages.warning(request, 'Budget not added, something wrong!')
        return redirect('utils:add_budget')
    
    return render(request, 'utils/budget_list.html', context={'budgets':budgets})
    