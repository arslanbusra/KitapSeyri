from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import UserRegisterForm
from sellbook.models import SellBook
from payment.models import PaymentOrder
from activity.models import Event, Participant
from .models import Profile

# Kullanıcı Kaydı
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user) 
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('profile')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f"{field.label}: {error}")
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
            for field in form:
                for error in field.errors:
                    messages.error(request, f"{field.label}: {error}")
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
    user_books = SellBook.objects.filter(seller=request.user)
    orders = PaymentOrder.objects.filter(user=request.user)
    joined_events = Event.objects.filter(participants__user=request.user)

    context = {
        'orders': orders,
        'user_books': user_books,
        'joined_events': joined_events,
    }
    return render(request, 'profile.html', context)
