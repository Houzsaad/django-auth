#from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from accounts.models import Memmber, User, CEO

from .form import CEOForm

from .form import RegistrationForm

#@login_required
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
           user = form.save()
           login(request, user)
           return redirect('profile')
            
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def login_view(request):
    if request.method == 'POST':
        # Handle login logic here
        username = request.POST.get['username']
        password = request.POST.get['password']

        #jango handles password checking securely
        user =  authenticate (request, username=username, password=password)

        if user is not None:
            login(request, user) #create session
            return redirect('profile')         

        else:
            return render(request, 'accounts/login.html', {'error': 'invalid credentials'})
    
    return render(request, 'accounts/login.h66tml')

def logout_view(request):
    logout(request)
    return render(request, 'logged_out.html')


def user_list(request):
    users = User.objects.all()

    return render(request, 'accounts/user_list.html', {'users': users})

def memmber(request):
    memmbers = Memmber.objects.all()
    
    #if request.method == 'POST':
        #member.name = request.POST.get('name')
        #member.save()

    return render(request, 'accounts/memmber.html', {'memmbers': memmbers})

def ceo(request):
    ceos = CEO.objects.all()

    return render(request, 'accounts/ceo.html', {'ceos': ceos})

@login_required(login_url='login')
def profile(request):
    return render(request, 'accounts/profile.html')


def add(request):
    form = CEOForm()
    #form = CEOForm(request.Post)

    if request.method == 'POST':
        form=CEOForm(request.POST)
        if form.is_valid():
            #ceo = CEOForm()
            form.save()
            return redirect('user_list')
    context = {'form': form}    #else:
        #ceo = CEOForm()
            #form.save()
    return render(request, 'accounts/add-form.html', context)

def delete(request, pk):
    ceo = CEO.objects.get(id=pk)
    if request.method == 'POST':
        ceo.delete()
        return redirect('ceo')
    return render(request, 'accounts/delete-form.html', {'obj': ceo})


def update(request, pk):

    ceo = CEO.objects.get(id=pk)
    form = CEOForm(instance=ceo)

    if request.method == 'POST':
        form = CEOForm(request.POST, instance=ceo)
        if form.is_valid():
            form.save()
            return redirect('ceo')
    else:
        form = CEOForm(instance=ceo)
        context = {'form': form}
        return render(request, 'accounts/update-form.html', {'form': form})