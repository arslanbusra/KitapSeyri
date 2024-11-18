from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SellBook, Category, Language
from .forms import SellBookForm

@login_required(login_url='/login/')
def sellbook(request):
    if request.method == 'POST':
        form = SellBookForm(request.POST, request.FILES)
        if form.is_valid():
            new_book = form.save(commit=False)
            new_book.seller = request.user
            new_book.save()
            return redirect('buybook')
    else:
        form = SellBookForm()

    return render(request, 'sellbook.html', {'form': form})











