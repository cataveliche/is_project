from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def home(request):
	return render(request, 'authenticate/home.html',{})

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('You have Been Logged In!'))
			return redirect('home')
		else:
			messages.success(request, ('Error, try again'))
			return redirect('login')
	else:
		return render(request, 'authenticate/login.html',{})

def logout_user(request):
	logout(request)
	return redirect('home')
def cell_control(request):
	return render(request, 'authenticate/cycle_control.html',{})
def register_user(request):
	if request.method =="POST":
		form= UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username= form.cleaned_data['username']
			password= form.cleaned_data['password1']
			user = authenticate( username=username, password=password)
			login(request, user)
			return redirect('home')
	else:
		form=UserCreationForm()
		
	context = {'form': form}
	return render(request, 'authenticate/register.html',context)