from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LogInForm, PLogInForm


app_name= 'core'

urlpatterns= [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('clientsignup/', views.UserSignUp, name= 'UserSignUp'),
    path('login/', auth_views.LoginView.as_view(template_name= 'core/login.html',authentication_form= LogInForm), name='login'),
    path('elogin/', auth_views.LoginView.as_view(template_name= 'core/elogin.html',authentication_form= PLogInForm), name='elogin'),
    path('logout/', views.logout_user, name='logout'),
]   