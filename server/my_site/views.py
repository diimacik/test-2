from django.shortcuts import render
from .models import NewsAdmin

# Create your views here.
def index(request):
    news = NewsAdmin.objects.all()
    return render (request, 'index.html', {'news':news})

def about(request):
    return render (request, 'about.html')