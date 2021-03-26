from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm, FixtureForm
from .models import Video, Team, User, Fixture
from .decorators import allowed_users


def index(request):
	return render(request, 'Team/index.html')

def registration_view(request):
	context = {}
	if request.POST:
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			email        = form.cleaned_data.get('email')
			first_name   = form.cleaned_data.get('first_name')
			last_name    = form.cleaned_data.get('last_name')
			raw_password = form.cleaned_data.get("password1")
			account      = authenticate(email=email, first_name=first_name, last_name=last_name, password=raw_password)

			if form.cleaned_data.get('user_type') == 'CO':
				user.is_coach = True

			login(request, account)
			return redirect('<str:room_name>/')
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
	room_name = Team.objects.values('code')
	fixtureDisplay = Fixture.objects.all()
	return render(request, 'Team/room.html', {'room_name': room_name, 'fixture': fixtureDisplay })
