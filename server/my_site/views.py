from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import NewsAdmin

# Create your views here.
def index(request):
    news = NewsAdmin.objects.all()
    return render (request, 'index.html', {'news':news})

def about(request):
    return render (request, 'about.html')

def profile(request):
    return render (request, 'profile.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Have Logged In! Welcome!'))
            return redirect('index')
        else:
            messages.success(request, ('There was an error loggin in Please try Againg'))
            return redirect('login')
    else:
        return render (request, 'login.html', {})