from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.
def homepage(request):
	return render(request=request, 
					template_name = "main/home.html",
					context = {"tutorials": Tutorial.objects.all})

def register(request):
	if request.method == "POST":
		'''
		So when user is logging in then we are sending information to 
		alter the current database.
		so this is a post type request.
		'''
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get("username")
			messages.success(request,f"New user created: {username}")
			login(request,user)
			messages.info(request, f"You are now logged in as {username}")
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request,f"{msg}:{form.error_messages[msg]}")

	form = UserCreationForm
	return render(request,"main/register.html",context = {"form":form})