from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SellBook, Category, Language

@login_required
def sellbook(request):
    if request.method == 'POST':
        bookname = request.POST['bookname']
        authorname = request.POST['authorname']
        price = request.POST['price']
        discount = request.POST['discount']
        booktype_id = request.POST['booktype']
        booklang_id = request.POST['booklang']
        bookimage = request.FILES['bookimage']

        booktype = Category.objects.get(id=booktype_id)
        booklang = Language.objects.get(id=booklang_id)
        
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
        return redirect('profile')
        
    categories = Category.objects.all()
    languages = Language.objects.all()

    context = {
        'categories': categories,
        'languages': languages
    }
    return render(request, 'sellbook.html', {'categories': categories, 'languages': languages})


