from django.shortcuts import render,redirect
from sellbook.models import SellBook
from article.models import Article
from .models import City, ContactMessage
from .forms import ContactForm
from django.contrib import messages


def index(request):
    favorite_books = SellBook.objects.all()[:3] 
    articles = Article.objects.all()[:2] 
    context = {
        'favorite_books': favorite_books,
        'articles': articles,
    }
    return render(request, 'index.html', context)
    
def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save(commit=False)
            if request.user.is_authenticated:
                contact_message.user = request.user
            contact_message.save()
            messages.success(request, 'Talebiniz alınmıştır.', extra_tags='bold')
            return redirect('contact')
    else:
        form = ContactForm()
    
    cities = City.objects.all()
    return render(request, 'contact.html', {'form': form, 'cities': cities})












