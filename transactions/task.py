from celery import shared_task
from datetime import date
from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task(bind=True)
def Shadule_Transection(self, send_user, receive_user, account_number, float_amount, note):
    from .models import Transaction, TotalBalance
    from django.contrib.auth import get_user_model

    # get user model
    
    
    # get send user and receive user obj
    send_user = User.objects.get(id=send_user)
    receive_user = User.objects.get(id=receive_user)
    
    sender_total_balance = TotalBalance.objects.get(user=send_user)
    receiver_total_balance = TotalBalance.objects.get(user=receive_user)
    
    # save transection data to the database
    
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
    
    print(account_number, float_amount, note)
    return "Task Successfully shaduled!"


@shared_task(bind=True)
def BudgetReminder(self):
    from utils.models import Budget
    User = get_user_model()
    today = date.today()
    users = User.objects.filter(budget__due_date=today).distinct()
    
    for user in users:
        due_budgets = Budget.objects.filter(user=user, due_date=today)
        if due_budgets.exists():
            budget_list = "\n".join([f"- {b.title} User: {user.username}" for b in due_budgets])
            message=f"Hi {user.username},\n\nHere are your budgets due today:\n\n{budget_list}\n\n- Your Daily Tracker"
            print(message)
    return "BudgetReminder task successfully execute!"



