from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Q
# Create your views here.


def add_budget_cat(request):
    try:
        user = request.user
    except Exception as e:
        messages.error(request, f"User  Does not matching.error: {e}")
    if request.method == "POST":
        cat_name = request.POST.get('cat_name')
        print("''''''''=")
        print(cat_name)
        
    return render (request, 'utils/budget_cat_add.html', context={})
    