from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import BudgetCategory, Budget, SheduleMail, Note
from .forms import ShedulemailForm, NoteForm
# Create your views here.

@login_required
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
    
    

@login_required
def view_budget_category(request):
    user = request.user
    try:
        budget_categorys = BudgetCategory.objects.filter(user = user)
    except Exception as e:
        messages.warning(request, F"Something wrong!Error:{e}")
        return redirect('utils:add_budget_cat')
    return render(request, 'utils/budget_cat.html', context={"categorys":budget_categorys})


@login_required
def delete_budget_cat(request, id):
    user = request.user
    try:
        budget_category = BudgetCategory.objects.filter(Q(id=id) & Q(user=user)).first()
    except Exception as e:
        messages.error(request, f"Category not delete, Error: {e}!")
        return redirect('utils:category_list')
    budget_category.delete()
    messages.success(request, "Category successfully deleted!")
    return redirect('utils:category_list')


@login_required
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


@login_required
def view_budget(request):
    user = request.user
    
    try:
        budgets = Budget.objects.filter(user=user)
    except Exception as e:
        messages.warning(request, 'something wrong!')
        return redirect('utils:view_budget')
    
    return render(request, 'utils/budget_list.html', context={'budgets':budgets})


@login_required
def update_to_complate(request, id):
    user = request.user
    try:
        budget = Budget.objects.filter(Q(id=id) & Q(user=user)).first()
    except Exception as e:
        messages.error(request, 'something wrong!')
        return redirect('utils:view_budget')

    budget.is_completed = True
    budget.save()
    messages.success(request, 'Successfully updated!')
    return redirect('utils:view_budget')
    

@login_required
def delete_budget(request, id):
    user = request.user
    try:
        budget = Budget.objects.filter(Q(id=id) & Q(user=user)).first()
    except Exception as e:
        messages.error(request, 'something wrong!')
        return redirect('utils:view_budget')

    budget.delete()
    messages.success(request, 'Budget successfully deleted!')
    return redirect('utils:view_budget')

@login_required
def SendMail(request):
    if request.method == 'POST':
        form_data = ShedulemailForm(request.POST)
        print(form_data)
        if form_data.is_valid():
            shedule_mail = form_data.save(commit=False)  # Don't save to DB yet
            shedule_mail.user = request.user  # Assign logged-in user
            shedule_mail.save()  # Now save it to the databas
            messages.success(request, "Mail Successfully Sheduled!")
            return redirect('utils:send_mail')
        else:
            messages.error(request, "Email Not Shedule, Something Wrong!")
            return redirect('utils:send_mail')
    form = ShedulemailForm()
    return render(request, 'utils/sendmail.html', context = {'form':form})

@login_required
def SentMail(request):
    user = request.user
    sent_mails = SheduleMail.objects.filter(Q(is_sent=True) & Q(user=user))
    return render(request, 'utils/sentmail.html', context={'sent_mails':sent_mails})



@login_required
def DeleteMail(request, id):
    user = request.user
    try:
        mail = SheduleMail.objects.filter(Q(id=id) & Q(user=user)).first()
    except Exception as e:
        messages.error(request, f"Mail not delete, Error: {e}!")
        return redirect('utils:sent_mail')
    mail.delete()
    messages.success(request, "Mail successfully deleted!")
    return redirect('utils:sent_mail')


@login_required
def AddNote(request):
    if request.method == "POST":
        form_data = NoteForm(request.POST)
        if form_data.is_valid():
            note = form_data.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, "Note Successfully added")
            return redirect('utils:add_note')
        else:
            messages.error(request, "Note Not save!", form_data.errors)
            return redirect('utils:add_note')
    form = NoteForm()
    return render(request, 'utils/add_note.html', context={'form':form})