from django.shortcuts import render

# Create your views here.


def Dashbord(request):
    return render(request, 'Home/dashbord.html')