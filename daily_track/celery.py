import os

from celery import Celery
from celery.schedules import crontab
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'daily_track.settings')

app = Celery('daily_track')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()




app.conf.beat_schedule = {
    'budget_reminder_shadule': {
        'task': 'transactions.task.BudgetReminder',
        'schedule': crontab(hour=23, minute=17),
    },
    'future_work_reminder_shadule': {
        'task': 'utils.tasks.DailyWorkRemainder',
        'schedule': crontab(hour=1, minute=4),
    },
    'project_reminder_shadule': {
        'task': 'utils.tasks.ProjectPlanRemainder',
        'schedule': crontab(hour=1, minute=19),
    },
}

