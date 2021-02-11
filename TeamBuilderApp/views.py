from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, FixtureForm
from .models import Video, Team, User

def index(request):
	return render(request, 'Team/index.html')

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
			return redirect(User.team.code)
		else:
			context['registration_form'] = form
	else:
		form = CustomUserCreationForm
		context['registration_form'] = form
	return render(request, 'Team/register.html', context)

def fixture_view(request):
	context = {}
	if request.POST:
		fixture = FixtureForm(request.POST)
		if fixture.is_valid():
			fixture.save()
			address_1 = form.cleaned_data.get('address_1')
			address_2 = form.cleaned_data.get('address_2')
			city      = form.cleaned_data.get('city')


def main(request):
    return render(request, "Team/mainpage.html")

def logout_user(request):
	logout(request)
	messages.info(request, "Logged out successfully")
	return redirect('/Team')

def room(request, room_name):
    return render(request, 'Team/room.html', {
        'room_name': room_name
    })
