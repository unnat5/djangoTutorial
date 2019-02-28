from django.shortcuts import render
from django.http import HttpResponse 

def homepage(request):
	return HttpResponse("This is our <strong>homepage</strong>!")
# Create your views here.
