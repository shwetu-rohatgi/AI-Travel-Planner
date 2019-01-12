from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(response):
	return render(response, 'home/home.html')   #it actually goes to home/templates/home.html

def search(response):
	return render(response, 'home/search.html') 