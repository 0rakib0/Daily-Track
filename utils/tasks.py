from celery import shared_task
from django.contrib.auth import get_user_model

from datetime import date



@shared_task(bind=True)
def SendMial(self, subject, message, sent_from, sent_to):
    print(f"Subject: {subject} | Messsage: {message} | Sent From: {sent_from} | Sent To: {sent_to}")
    return "Email Successfully Send to the user"


@shared_task(bind=True)
def DailyWorkRemainder(self):
    from .models import FutureWork
    User = get_user_model()
    today = date.today()
    shadule_work_users = User.objects.filter(user_future_work__shedule_date=today).distinct()
    for user in shadule_work_users:
        future_works = FutureWork.objects.filter(user=user, shedule_date=today)
        if future_works.exists():
            future_work_list = "\n".join([f"- {f.title} User: {user.username}" for f in future_works])
            print(future_work_list)
    
    return "Dailly Task Reminder==========="


@shared_task(bind=True)
def ProjectPlanRemainder(self):
    from .models import ProjectPlan
    User = get_user_model()
    today = date.today()
    users_projects_plans = User.objects.filter(project_plan__date=today).distinct()
    for user in users_projects_plans:
        project_plans = ProjectPlan.objects.filter(user=user, date=today)
        if project_plans.exists():
            project_plan_list = "\n".join([f"- {f.project.project_name} User: {user.username}" for f in project_plans])
            print(project_plan_list)
    
    return "Dailly Task Reminder==========="