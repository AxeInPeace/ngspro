from django.contrib.auth import *
from django.shortcuts import render
from models import *
from forms import *
from lib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect


def map(request):
	baloons = baloon.objects.all()
	if request.method == "GET":
		
		if request.user.is_authenticated():
			frmat = formats.objects.all()
			tools = instruments.objects.all()
			my_rating = User.objects.get(django_user=request.user).getRating()
			
			context = {		
				"formats": frmat,
				"tools": tools,
				"baloons": baloons,
				"signin_error": None,
				"my_rating": my_rating,				
				"user": request.user,			
			}
			return render(request, 'index.html', context)		
		context = {		
			"baloons": baloons,
			"signin_error": None,
			"signin_form": SigninForm(),
		}
		return render(request, 'ind.html', context)

	
	if request.method == "POST":
		signin_form = SigninForm(request.POST)
		#check login
		try:
			logn = signin_form.data["login"]
		except:			
			context = {
				"baloons": baloons,
				"signin_error": "Please enter your login",
			}
			return render(request, 'index.html', context)
		
		#check pass
		try:
			password = signin_form.data["password"]
		except:			
			context = {
				"baloons": baloons,
				"signin_error": "Please enter your password",
			}
			return render(request, 'index.html', context)
		
		#check user
		user = authenticate(username=logn, password=password)
		if user is None:
			context = {			
				"baloons": baloons,
				"signin_error": "Wrong login or pass",			
			}
			return render(request, 'index.html', context)	

		login(request, user)
		my_rating = custom_user.objects.get(user=request.user).getRating()
		context = {		
				"baloons": baloons,
				"signin_error": None,
				"my_rating": my_rating,
				"user": request.user,
			}
		
		return render(request, 'index.html', context)
		
		if purpose == "add_baloon":	
			try:
				c1 = request.GET['coord1']
				c2 = request.GET['coord2']
				us = custom_user.objects.get(user=request.user)
				date = request.GET['day'] + "-" + request.GET['month'] + "-" + request.GET['year']
				ug = request.GET['ug']
				hz = request.GET['hz']
				tool = request.GET['tool']
				frmat = request.GET['format']
			except:
				context = {
					"baloons": baloons,
					"signin_error": "Wrong form",
				}
				return render(request, 'index.html', context)
			tl = instruments.objects.get(name=tool)
			fm = formats.objects.get(name=frmat)
			baloon.objects.create(
				coord1=c1, 
				coord2=c2, 
				date=date, 
				publisher=us,
				hasundergrshoot=ug,
				hashorizontals=hz,
				instrument=tl,
				format=fm					
			)

def registration(request):	
	if request.method == "GET":
		context = {
			"signup_form": SignupForm(),
		}
		return render(request, 'signup.html', context)

	if request.method == "POST":
		signup_form = SignupForm(request.POST)
		user_login = signup_form.data["login"]
		if User.objects.filter(username = user_login):
			context = {
				"login": request.user.username,
				"signup_form": SignupForm(),
				"signup_error": "This login is already reserved",
			}		
			return render(request, 'signup.html', context)

		user_mail = signup_form.data["mail"]
		if User.objects.filter(email = user_mail):
			context = {
				"login": request.user.username,
				"signup_form": SignupForm(),
				"signup_error": "This e-mail is already reserved",
			}		
			return render(request, 'signup.html', context)

		if signup_form.data["password"] != signup_form.data["confirm_password"]:
			context = {
				"login": request.user.username,
				"signup_form": SignupForm(),
				"signup_error": "Pass don't match",
			}		
			return render(request, 'signup.html', context)
				
		try:
			new_user = User.objects.create_user(user_login, user_mail, signup_form.data["password"])
			custom_user.objects.create(userowner=new_user, rating=0)
		except BaseException:
			context = {
				"login": request.user.username,
				"signup_form": SignupForm(),
				"signup_error": "Registration error",
			}		
			return render(request, 'signup.html', context)
		
		return HttpResponseRedirect("/")


def fun_logout(request):
	logout(request)	
	return HttpResponseRedirect("/")


