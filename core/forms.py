from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LogInForm(AuthenticationForm):
        username= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Username', 'class': 'w-full py-4 px-6 rounded-xl'}))
        password= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class': 'w-full py-4 px-6 rounded-xl'}))

class PLogInForm(AuthenticationForm):
     employee_ID= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Employee ID', 'class': 'w-full py-4 px-6 rounded-xl'}))
     access_key= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Access Key provided to you', 'class': 'w-full py-4 px-6 rounded-xl'}))
     


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'names','email', 'password1', 'password2')
    username= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Username', 'class': 'w-full py-4 px-6 rounded-xl'}))
    email= forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter email', 'class': 'w-full py-4 px-6 rounded-xl'}))
    password1= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password (must have unique symbols such as @,#,$,%)', 'class': 'w-full py-4 px-6 rounded-xl'}))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password', 'class': 'w-full py-4 px-6 rounded-xl'}))
    names = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Name as it appears on Gov.Issued ID', 'class': 'w-full py-4 px-6 rounded-xl'}))