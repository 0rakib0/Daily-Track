from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import logging

# Optional: Set up logging
logger = logging.getLogger(__name__)




def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')
        
        if not username or not password or not confirm_password:
            messages.error(request, 'All fields are required.')
            return redirect('register_user')

        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters.')
            return redirect('register_user')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register_user')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return redirect('register_user')

        hashed_password = make_password(password)
        user = User.objects.create(username=username, password=hashed_password)
        user.save()
        messages.success(request, 'Your Account successfully registered, Please complate your profile.')
        return redirect('login_page')
    return render(request, 'shared/register.html')

def Login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You are successfully logged in.')
            return redirect('Home:dashbord')
        else:
            # Optional: Log failed login attempts for debugging or security purposes
            logger.warning(f"Failed login attempt with username: {request.POST.get('username')}")
            
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('login_page')
    else:
        form = AuthenticationForm()  # Create an empty form for GET requests

    return render(request, 'shared/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, "Successfully loged out!")
    return redirect('login_page')
