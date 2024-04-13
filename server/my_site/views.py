from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import NewsAdmin
from .forms import SignUpForm

# Create your views here.
def index(request):
    news = NewsAdmin.objects.all()
    return render (request, 'index.html', {'news':news})

def NewsPost(request, pk):
    news = NewsAdmin.objects.get(id=pk)
    return render (request, 'news-admin.html', {'news':news})

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
    
def logout_user(request):
    logout(request)
    return redirect('index')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #first_name = form.cleaned_data['first_name']
            #last_name = form.cleaned_data['last_name']
            #email = form.cleaned_data['email']
            # Login in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You have successfully reqisterd! Wellcom'))
            return redirect ('index')
    return render(request, 'register.html', {'form':form})