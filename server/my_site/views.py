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

def delete_comment(request, pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, id=pk)
        # Check to see if you own the comment
        if request.user.username == comment.author.username:
            # Delete the Comment
            comment.delete()
            messages.success(request, ('The Comment has been Deleted!'))
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.success(request, ("You Don't Own That Comment!"))
            return redirect('index')
    else:
        messages.success(request, ("Please Log In To Continue..."))
        return redirect(request.META.get('HTTP_REFERER'))
    
def edit_comment(request, pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, id=pk)
        if request.user.username == comment.author.username:
            form = CommentForm(request.POST or None, instance=comment)
            if request.method == 'POST':
                if form.is_valid():
                    comment = form.save(commit=False)
                    comment.author = request.user
                    comment.save()
                    messages.success(request, ("YOUR Comment has been Updated!"))
                    return redirect('admin-post', pk=comment.post.pk)
            else:
                return render(request, 'edit_comment.html', {'form':form, 'comment':comment, })
        else:
            messages.success(request, ("You Don't Own That Comment!"))
            return redirect('index')
    else:
        messages.success(request, ("Please Log In To Continue..."))
        return redirect('index')
    
        


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