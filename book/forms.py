from django import forms
from book.models import Book


class Create_book(forms.ModelForm):
   class Meta:
      model = Book
      fields = "__all__"