from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
	first_name = forms.CharField( max_length=30)
	last_name = forms.CharField(max_length=30)
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
		

class updateUserData(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email']



class updateProfileData(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['image', 'date']