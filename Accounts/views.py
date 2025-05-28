from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'home.html')
        else:
            messages.error(request, 'Invalid form submission. Please try again.')
    else:
        form= UserCreationForm()
    return render(request, 'signup.html', {'form': form})
    

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid form submission. Please try again.')
    else:
        form= AuthenticationForm()
    return render(request, 'signin.html', {'form': form})
    

def Logout(request):
    logout(request)
    return redirect('login')