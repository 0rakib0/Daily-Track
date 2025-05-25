from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import BudgetCategory, Budget, SheduleMail, Note, Tasks, FutureWork, Project, ProjectPlan
from .forms import ShedulemailForm, NoteForm, TasksForm, FutureWorkForm, ProjectForm, ProjectPlanForm
from datetime import date
from .task import test_task
from django.http import HttpResponse
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


@login_required
def ViewNote(request):
    user = request.user
    user_notes = Note.objects.filter(user=user)
    return render(request, 'utils/view_note.html', context={'user_notes':user_notes})


@login_required
def UpdateNote(request, id):
    user = request.user
    try:
        note = Note.objects.filter(Q(id=id) & Q(user=user)).first()
        if not note:
            messages.error(request, "Note Not Found!")
            return redirect('utils:view_note')
    except Exception as e:
        messages.error(request, f"Error fetching note: {e}")
        return redirect('utils:view_note')
    
    if request.method == "POST":
        update_data = NoteForm(request.POST, instance=note)
        if update_data.is_valid():
            update_data.save()
            messages.success(request, "Note sucessfully updated!")
            return redirect('utils:view_note')
    form = NoteForm(instance=note)
    return render(request, 'utils/update_note.html', context={'form':form})



@login_required
def DeleteNote(request, id):
    user = request.user
    try:
        note = Note.objects.filter(Q(id=id) & Q(user=user)).first()
    except Exception as e:
        messages.error(request, f"Note not delete, Error: {e}!")
        return redirect('utils:view_note')
    note.delete()
    messages.success(request, "Note successfully deleted!")
    return redirect('utils:view_note')


@login_required
def AddTask(request):
    if request.method == "POST":
        form_data = TasksForm(request.POST)
        if form_data.is_valid():
            tasks = form_data.save(commit=False)
            tasks.user = request.user
            tasks.save()
            messages.success(request, "Tasks Successfully added")
            return redirect('utils:add_task')
        else:
            messages.error(request, "Tasks Not save!", form_data.errors)
            return redirect('utils:add_task')
    form = TasksForm()
    return render(request, 'utils/add_tasks.html', context={'form':form})


@login_required
def ViewPendingTask(request):
    user = request.user
    tasks = Tasks.objects.filter(Q(user=user) & Q(is_complated=False))
    if not tasks:
        messages.error(request, "There is no pending task available!")
    
    return render(request, 'utils/view_pending_tasks.html', context={'tasks':tasks})

@login_required
def ViewComplateTask(request):
    user = request.user
    tasks = Tasks.objects.filter(Q(user=user) & Q(is_complated=True))
    if not tasks:
        messages.error(request, "There is no Complate task available!")
    
    return render(request, 'utils/view_complate_tasks.html', context={'tasks':tasks})


@login_required
def DeleteTask(request, id):
    user = request.user
    try:
        task = Tasks.objects.filter(Q(id=id) & Q(user=user)).first()
    except Exception as e:
        messages.error(request, f"Task not delete, Error: {e}!")
        return redirect('utils:view_pending_task')
    task.delete()
    messages.success(request, "Task successfully deleted!")
    return redirect('utils:view_pending_task')


@login_required 
def TaskUpdate(request, id):
    user = request.user
    try:
        task = Tasks.objects.filter(Q(id=id) & Q(user=user)).first()
    except Exception as e:
        messages.error(request, 'something wrong!')
        return redirect('utils:view_pending_task')

    task.is_complated = True
    task.save()
    messages.success(request, 'Successfully updated!')
    return redirect('utils:view_pending_task')
    
    
@login_required
def ShaduleFutureWork(request):

    if request.method == 'POST':
        form_data = FutureWorkForm(request.POST)

        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request, "Work successfully shaduled!")
            return redirect('utils:shaduel_work')
        else:
            messages.error(request, f'Somethingk wrong: {form_data.errors}')
            return redirect('utils:shaduel_work')

    form = FutureWorkForm()
    return render(request, 'utils/futureworkshedule.html', context={'form':form})


@login_required
def PendingShaduledWork(request):
    context = None
    pending_works = FutureWork.objects.filter(Q(user=request.user) & Q(is_done=False))
    if pending_works:
        context = {'pending_works':pending_works}
    else:
        messages.warning(request, 'No pending work available!')
    
    return render(request, 'utils/pending_work.html', context)


@login_required
def ComplateShaduleWork(request):
    complate_works = FutureWork.objects.filter(Q(user=request.user) & Q(is_done=True))
    if complate_works:
        context = {'complate_works':complate_works}
    else:
        messages.warning(request, 'No complate work available!')
    
    return render(request, 'utils/complate_work.html', context)



@login_required
def UpdateWork(request, id):
    try:
        pending_work = FutureWork.objects.filter(Q(user=request.user) & Q(id=id)).first()
        if pending_work:
            pending_work.is_done = True
            pending_work.save()
            messages.success(request, "Work successfully update to done!")
            return redirect("utils:pending_work")
    except FutureWork.DoesNotExist:
        messages.error(request, "Future Work Does not exit!")
        return redirect("utils:pending_work")

@login_required
def DeleteWork(request, id):
    try:
        work = FutureWork.objects.filter(Q(user=request.user) & Q(id=id)).first()
        if work:
            work.delete()
            messages.success(request, "Work successfully deleted!")
            return redirect("utils:pending_work")
    except FutureWork.DoesNotExist:
        messages.error(request, "Future Work Does not exit!")
        return redirect("utils:pending_work")
    
    
@login_required
def AddProject(request):
    if request.method == 'POST':
        form_data = ProjectForm(request.POST)

        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request, "Project successfully added!")
            return redirect('utils:add_project')
        else:
            messages.error(request, f'Somethingk wrong: {form_data.errors}')
            return redirect('utils:add_project')
    form = ProjectForm()
    return render(request, 'utils/add_project.html', context={'form':form})


@login_required
def AllProject(request):
    projects_list = Project.objects.filter(Q(user=request.user))
    if projects_list:
        context = {'projects_list':projects_list}
    else:
        messages.warning(request, 'No projects available right now!')
    return render(request, 'utils/all_projects.html', context)


@login_required
def UpdateProject(request, id):
    try:
        project = Project.objects.filter(Q(user=request.user) & Q(id=id)).first()
        if not project:
            messages.error(request, "Project Not Found!")
            return redirect('utils:all_projects')
    except Exception as e:
        messages.error(request, f"Error fetching project: {e}")
        return redirect('utils:all_projects')
    
    if request.method == "POST":
        form_data = ProjectForm(request.POST, instance=project)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Project Successfully updated!")
            return redirect('utils:all_projects')
        else:
            messages.error(request, "Project not updated! somethink wrong!")
            return redirect('utils:all_projects')
    
    form = ProjectForm(instance=project)
    return render(request, 'utils/update_project.html', context={'form':form})



@login_required
def DeleteProject(request, id):
    try:
        project = Project.objects.filter(Q(user=request.user) & Q(id=id)).first()
    except Exception as e:
        messages.error(request, f'Somethingk wrong: {e}')
        return redirect('utils:add_project_plan')
    
    project.delete()
    messages.success(request, "Project Data successfully deleted!")
    return redirect('utils:all_projects')


@login_required
def AddProjectPlaning(request):
    if request.method == 'POST':
        form_data = ProjectPlanForm(request.POST)

        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request, "Project plan successfully added!")
            return redirect('utils:add_project_plan')
        else:
            messages.error(request, f'Somethingk wrong: {form_data.errors}')
            return redirect('utils:add_project_plan')
    form = ProjectPlanForm()
    return render(request, 'utils/add_project_plan.html', context={'form':form})



@login_required
def ViewPerojectPlan(request, id):
    todays_date = today = date.today()
    try:
        project = Project.objects.filter(Q(user=request.user) & Q(id=id)).first()
        project_plan = ProjectPlan.objects.filter(Q(project=project) & Q(user=request.user))
        todays_project_plan = ProjectPlan.objects.filter(Q(project=project) & Q(date=todays_date)).first()
    except Project.DoesNotExist:
        messages.error(request, "Project Does Not Fount, something wrong!")
        return redirect('utils:all_projects')
    
    print(project_plan)
    
    return render(request, 'utils/project_plans.html', context={'project_plan':project_plan, 'todays_project_plan':todays_project_plan})


@login_required
def UpdateProjectPlan(request, id):
    try:
        project_plan = ProjectPlan.objects.filter(Q(user=request.user) & Q(id=id)).first()
        if not project_plan:
            messages.error(request, "Project plan Not Found!")
            return redirect('utils:all_projects')
    except Exception as e:
        messages.error(request, f"Error fetching project: {e}")
        return redirect('utils:all_projects')
    
    if request.method == "POST":
        form_data = ProjectPlanForm(request.POST, instance=project_plan)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Project Plan Successfully updated!")
            return redirect('utils:all_projects')
        else:
            messages.error(request, "Project plan not updated! somethink wrong!")
            return redirect('utils:all_projects')
    
    form = ProjectPlanForm(instance=project_plan)
    return render(request, 'utils/update_project_plan.html', context={'form':form})


@login_required
def DeleteProjectPlan(request, id):
    try:
        project_plan = ProjectPlan.objects.filter(Q(user=request.user) & Q(id=id)).first()
    except Exception as e:
        messages.error(request, f'Somethingk wrong: {e}')
        return redirect('utils:add_project_plan')
    
    project_plan.delete()
    messages.success(request, "Project Data successfully deleted!")
    return redirect('utils:all_projects')











def test_celery(request):
    result = test_task.delay()
    return HttpResponse("Task Susseccfully shaduled!")