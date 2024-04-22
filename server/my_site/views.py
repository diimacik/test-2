from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import NewsAdmin, Comment
from .forms import SignUpForm, CommentForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    news = NewsAdmin.objects.all()
    return render (request, 'index.html', {'news':news})

def NewsPost(request, pk):
    news = NewsAdmin.objects.get(id=pk)
    comments = Comment.objects.filter(post=news)
    if request.user.is_authenticated:
        form = CommentForm(request.POST or None)
    # Handle comment submission
        if request.method == 'POST':
        
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.post = news
            
                
                new_comment.author = request.user
                new_comment.save()
                return redirect('admin-post', pk=pk)
            
            return redirect(request('index'))
    else:
        form = CommentForm()
    return render (request, 'news-admin.html', {'news':news, 'comments':comments, 'form':form})

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