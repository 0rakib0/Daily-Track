from django.urls import path
from . import views

app_name='utils'

urlpatterns = [
    path('add-budget-category/', views.add_budget_cat, name='add_budget_cat'),
    path('budget-category-list/', views.view_budget_category, name='category_list'),
    path('add-budget/', views.add_badget, name='add_budget'),
    path('view-budget-list/', views.view_budget, name='view_budget'),
    path('delete-budget-category/<id>/', views.delete_budget_cat, name='delete_category'),
    path('update-to-complate/<id>/', views.update_to_complate, name='update_to_complate'),
    path('delete-budget/<id>/', views.delete_budget, name='delete_budget'),
    path('shedule-mail/', views.SendMail, name='send_mail'),
    path('sent-mail-list/', views.SentMail, name='sent_mail'),
    path('delete-mail/<id>/', views.DeleteMail, name='delete_mail'),
    path('add-note/', views.AddNote, name='add_note'),
    path('view-notes-list/', views.ViewNote, name='view_note'),
    path('delete-note/<id>/', views.DeleteNote, name='delete_note'),
    path('update-note/<id>/', views.UpdateNote, name='update_note'),
    path('add-task/', views.AddTask, name='add_task'),
    path('view-pending-task/', views.ViewPendingTask, name='view_pending_task'),
    path('view-complate-task/', views.ViewComplateTask, name='view_complate_task'),
    path('delete-task/<id>/', views.DeleteTask, name='delete_task'),
    path('task-update-to-complate/<id>/', views.TaskUpdate, name='update_task'),
    path('shadule-future-work/', views.ShaduleFutureWork, name='shaduel_work'),
    path('pending-work/', views.PendingShaduledWork, name='pending_work'),
    path('complate-work/', views.ComplateShaduleWork, name='complate_work'),
    path('update-work/<int:id>/', views.UpdateWork, name='update_work'),
    path('delete-work/<int:id>/', views.DeleteWork, name='delete_work'),
    path('add-project/', views.AddProject, name='add_project'),
    path('add-project-plan/', views.AddProjectPlaning, name='add_project_plan'),
    path('all-project-list/', views.AllProject, name='all_projects'),
    path('updat-project/<int:id>/', views.UpdateProject, name='update_project'),
    path('delete-project/<int:id>/', views.DeleteProject, name='delete_project'),
    path('view-project-plan/<int:id>/', views.ViewPerojectPlan, name='view_project_plan'),
    path('update-project-plan/<int:id>/', views.UpdateProjectPlan, name='update_project_plan'),
    path('delete-project-plan/<int:id>/', views.DeleteProjectPlan, name='delete_project_plan'),
    

]