from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm, UpdateUserForm, UpdateProfilePicForm
from . models import Profile
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):    
    return render(request, 'apple/index.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST) # createuserform is going to expect data here
        if form.is_valid():
            # ensuring user who has just registered to our site is 
            current_user = form.save(commit=False)
            form.save()
            # asigned a default profile picture defined earlier, each time a user is created, linked to
            profile = Profile.objects.create(user=current_user)
            return redirect("my-login")
    context = {'form': form}
    return render(request, 'apple/register.html', context=context)


@login_required(login_url='my-login')
def dashboard(request):
    profile_pic = Profile.objects.get(user=request.user)
    context = {'profilePic':profile_pic}
    return render(request, 'apple/dashboard.html', context=context)


@login_required(login_url='my-login') # to protect the view, user must have an account and signed in to look at these
def profile_management(request):
    user_form = UpdateUserForm(instance=request.user) # ensures getting a prepopulated form
    profile = Profile.objects.get(user=request.user)
    profile_form = UpdateProfilePicForm(instance=profile) # user geting their profile pic after log in
    if request.method == 'POST':
        user_form=UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfilePicForm(request.POST, request.FILES, instance=profile) # when posting a new image, we are posting it - equest.POST, then manage it-request.FILES and make sure it is for the logged in user-instance=profile
        if user_form.is_valid():
            user_form.save()
            return redirect('dashboard')
        if profile_form.is_valid():
            profile_form.save()
            return redirect('dashboard')
    context = {'user_form': user_form, 'profile_form':profile_form}
    return render(request, 'apple/profile-management.html', context=context)


def my_login(request):
    form = LoginForm()
    if request.method =='POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")    
    context = {'form':form}
    return render(request, 'apple/my-login.html', context=context)


def user_logout(request):
    auth.logout(request)
    return redirect('')


@login_required(login_url='my-login')
def delete_account(request):
    if request.method =='POST':
         deleteUser = User.objects.get(username=request.user)
         deleteUser.delete()
         return redirect("")
    return render(request, 'apple/delete-account.html')
    
    
     
    