from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
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

        login_user = authenticate(request, username=username, password=password)

        if login_user:
            login(request, login_user)
            messages.success(request, 'Your Account successfully registered, Please complate your profile.')
            return redirect('update_profile')

    return render(request, 'shared/register.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Exist!")
            return redirect('update_profile')
        
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        messages.success(request, "Profile Information successfully updated!")
        return redirect('complate_profile')
    return render(request, 'accounts/update_profile.html')


@login_required
def complate_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        image = request.FILES.get('profile_image')
        bio = request.POST.get('bio')
        address = request.POST.get('address')

        profile.profile_pic = image
        profile.bio = bio
        profile.adress = address

        profile.save()
        messages.success(request, "Your Profile setup completed!")
        return redirect('Home:dashbord')
    return render(request, 'accounts/complate_profile.html')




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

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Successfully loged out!")
    return redirect('login_page')
