from django.shortcuts import render, redirect
from sellbook.models import SellBook
from buybook.models import Order
from django.contrib.auth.decorators import login_required

def index(request):
    favorite_books = SellBook.objects.all()[:3]  # İlk 3 kitabı getiriyoruz, siz ihtiyacınıza göre sayıyı ayarlayabilirsiniz
    context = {
        'favorite_books': favorite_books,
    }
    return render(request, 'index.html', context)
    
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

@login_required
def sellbook(request):
    if request.method == 'POST':
        # Kitap satma formu gönderildiyse
        bookname = request.POST['bookname']
        authorname = request.POST['authorname']
        price = request.POST['price']
        discount = request.POST['discount']
        booktype = request.POST['booktype']
        booklang = request.POST['booklang']
        bookimage = request.FILES['bookimage']
        
        new_book = SellBook(
            bookname=bookname,
            authorname=authorname,
            price=price,
            discount=discount,
            booktype=booktype,
            booklang=booklang,
            bookimage=bookimage,
            seller=request.user
        )
        new_book.save()
        return redirect('profile')  # Başarılı sayfasına yönlendirin
        
    return render(request, 'sellbook.html')


