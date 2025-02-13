from django.shortcuts import render

# Create your views here.


def Login_page(request):
    return render(request, 'shared/login.html')