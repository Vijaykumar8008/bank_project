from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.shortcuts import render, redirect
from .models import UserRegistrationForm
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required

def login_view(request):
    #import pdb;pdb.set_trace()
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('homepage/')  # Redirect to a page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login_page.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'user_register.html', {'form': form})

@login_required
def show_homepage(request):
	response = render(request, 'home_page.html')
	response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	response['Pragma'] = 'no-cache'
	response['Expires'] = '0'
	return response

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')