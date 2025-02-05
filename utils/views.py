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
    