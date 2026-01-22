from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

from accounts.models import Memmber, User, CEO


@login_required
def profile(request):
    return render(request, 'profile.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        # Handle login logic here
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')

    else:
        return render(request, 'login.html')

def logout_view(request):
    return render(request, 'logout.html')



def user_list(request):
    users = User.objects.all()

    return render (request, 'accounts/user_list.html',{'users': users})

def memmber(request):
    memmber = Memmber.objects.all()

    return render (request, 'accounts/memmber.html',{'memmber': memmber})

def ceo(request):
    ceo = CEO.objects.all()

    return render (request, 'accounts/ceo.html',{'ceo': ceo})

def profile(request):
    return render(request, 'accounts/profile.html')