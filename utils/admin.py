from django.contrib import admin
from utils.models import Budget, BudgetCategory, SheduleMail, Tasks, Note, FutureWork, Project, ProjectPlan
# Register your models here.

admin.site.register(Budget)
admin.site.register(BudgetCategory)
admin.site.register(SheduleMail)
admin.site.register(Tasks)
admin.site.register(Note)
admin.site.register(FutureWork)
admin.site.register(Project)
admin.site.register(ProjectPlan)