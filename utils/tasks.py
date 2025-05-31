from celery import shared_task
from django.contrib.auth import get_user_model
from datetime import date
from django.conf import settings
from django.core.mail import send_mail


@shared_task(bind=True)
def SendMial(self, subject, message, sent_from, sent_to, shadule_mail_id):
    from .models import SheduleMail
    send_mail(
        subject=f"🔔{subject}",
        message=message,
        from_email=sent_from,
        recipient_list=[sent_to],
        fail_silently=True
    )
    mail_instance = SheduleMail.objects.get(id=shadule_mail_id)
    mail_instance.is_sent = True
    mail_instance.save()
    return "Email Successfully Sent to the user"


@shared_task(bind=True)
def DailyWorkRemainder(self):
    from .models import FutureWork
    User = get_user_model()
    today = date.today()
    shadule_work_users = User.objects.filter(user_future_work__shedule_date=today).distinct()
    for user in shadule_work_users:
        future_works = FutureWork.objects.filter(user=user, shedule_date=today)
        if future_works.exists():
            future_work_list = "\n".join([f"- {f.title}" for f in future_works])
            send_mail(
                subject="🔔 Your Todays Work List - You Need to complate all work today",
                message=f"Hi {user.username},\n\nHere are your work due today:\n\n{future_work_list}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=True
            )
    
    return "Dailly Task Reminder"


@shared_task(bind=True)
def ProjectPlanRemainder(self):
    from .models import ProjectPlan
    User = get_user_model()
    today = date.today()
    users_projects_plans = User.objects.filter(project_plan__date=today).distinct()
    for user in users_projects_plans:
        project_plans = ProjectPlan.objects.filter(user=user, date=today)
        if project_plans.exists():
            project_plan_list = "\n".join([f"- {f.topic_list}" for f in project_plans])
            send_mail(
                subject="🔔 Your Todays Project plan list - You Need to complate today",
                message=f"Hi {user.username},\n\nHere are your todays project plan:\n\n{project_plan_list}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=True
            )
    
    return "Dailly Task Reminder==========="