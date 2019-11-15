from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'dynamicpystroke/index.html')

def register(request):
	return render(request, 'dynamicpystroke/register.html')

def login(request):
	return render(request, 'dynamicpystroke/login.html')