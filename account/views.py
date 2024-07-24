from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import UserRegisterForm

# Kullanıcı Kaydı
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('profile')
        else:
            messages.error(request, "Lütfen formu doğru doldurun.")
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

# Kullanıcı Girişi
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, "Kullanıcı adı veya şifre yanlış.")
        else:
            messages.error(request, "Lütfen formu doğru doldurun.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Kullanıcı Çıkışı
def logout_view(request):
    logout(request)
    return redirect('login')

# Kullanıcı Profili
@login_required
def profile(request):
    return render(request, 'profile.html')

