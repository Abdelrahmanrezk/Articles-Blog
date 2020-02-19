from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import  messages
from .forms import UserRegisterForm, updateUserData, updateProfileData
from django.contrib.auth.decorators import login_required
from .models import UserProfile



def user_register(request):
	if request.method == 'POST':
 		form = UserRegisterForm(request.POST)
 		if form.is_valid():
 			form.save()
 			username = form.cleaned_data.get('username')
 			messages.success(request, f'Now you have account so you can log in!!')
 			return redirect('user_login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

@login_required
def user_profile(request):
	if request.method == 'POST':
		user_form = updateUserData(request.POST, instance=request.user)
		user_profile_form = updateProfileData(
			request.POST,
			request.FILES,
			instance=request.user.userprofile
			)
		if user_form.is_valid() and user_profile_form.is_valid():
			user_form.save()
			user_profile_form.save()
			messages.success(request, f'Data updated success!! { request.user }')
			return redirect('user_profile')
	else:
		user_form = updateUserData(instance=request.user)
		user_profile_form = updateProfileData(instance=request.user.userprofile)
	contest = {
	'user_form': user_form,
	'user_profile_form': user_profile_form,
	}
	return render(request, 'users/profile.html', contest)