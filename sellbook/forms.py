from django import forms
from .models import SellBook

class SellBookForm(forms.ModelForm):
    class Meta:
        model = SellBook
        fields = ['bookname', 'authorname', 'price', 'discount', 'booktype', 'booklang', 'bookimage']

        labels = {
            'bookname': 'Kitap İsmi',
            'authorname': 'Yazar İsmi',
            'price': 'Fiyat',
            'discount': 'İndirim Oranı',
            'booktype': 'Kitap Kategorisi',
            'booklang': 'Kitap Dili',
            'bookimage': 'Kitap Fotoğrafı',
        }

