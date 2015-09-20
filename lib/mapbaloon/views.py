from django.shortcuts import render
from models import *

def map(request):
	
	baloons = baloon.objects.all()
	
	context = {		
		"baloons": baloons,
	}
	
	return render(request, 'index.html', context)

