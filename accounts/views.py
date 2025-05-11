from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def login_view(request):
    if request.user.is_authenticated:
        return redirect('music_player:index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('music_player:index')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'accounts/login.html')

@require_http_methods(['GET'])
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have successfully logged out.')
    return redirect('music_player:index')



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def register_view(request):
    if request.user.is_authenticated:
        return redirect('music_player:index')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('music_player:index')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})
