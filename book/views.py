from django.shortcuts import render
import json
from django.http import HttpResponse
import datetime
from django.template import loader
from book.models import Book





def current_datetime(request):
    print('request method is', request.method)
    now = datetime.datetime.now()
    html = 'this is MFT'
    return HttpResponse(html)


def current_datetime2(request):
    print('request method is', request.method)
    now = datetime.datetime.now()
    html = 'this is MFT sec'
    return HttpResponse(html)

def display_books(request):
  books = Book.objects.all().values()
  template = loader.get_template('All_books.html')
  context = {
    'mybook': books,
    
  }
  return HttpResponse(template.render(context, request))

