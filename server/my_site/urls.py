from django.urls import path
from . import views 

urlpatterns = [
    path('index', views.index, name='index'),
    path('admin-post/<int:pk>/', views.NewsPost, name='admin-post'),
    
    path('about', views.about, name='about'),
    path('profile', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]