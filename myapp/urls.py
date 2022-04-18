from django.urls import path
from . import views

urlpatterns = [
    path('', (views.index), name='index'),
    path('feed', (views.feed), name='feed'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signuppage'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]
