from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import Video

def index(request):
	return render(request, 'index.html')

def registration_view(request):
	context = {}
	if request.POST:
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			email        = form.cleaned_data.get('email')
			first_name   = form.cleaned_data.get('first_name')
			last_name    = form.cleaned_data.get('last_name')
			raw_password = form.cleaned_data.get("password1")
			account      = authenticate(email=email, first_name=first_name, last_name=last_name, password=raw_password)
			login(request, account)
			return redirect('/main/mainpage')
		else:
			context['registration_form'] = form
	else:
		form = CustomUserCreationForm
		context['registration_form'] = form
	return render(request, 'accounts/register.html', context)

def main(request):
    return render(request, 'main/mainpage.html')

def logout_user(request):
	logout(request)
	messages.info(request, "Logged out successfully")
	return redirect('/')

def display(request):
    videos = Video.objects.all
    return render(request, 'main/mainpage.html', {'videos':videos})