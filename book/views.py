from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
import datetime
from django.template import loader
from book.models import Book
from django.views.decorators.csrf import csrf_exempt
from book.forms import Create_book





def current_datetime(request):
    print('request method is', request.method)
    now = datetime.datetime.now()
    html = 'this is MFT'
    return HttpResponse(html)




def book_view(request):
   books=list(Book.objects.all().values())

   return JsonResponse(books , safe=False)

@csrf_exempt 
def add_book(request):
   if request.method == "POST":
      body = json.loads(request.body.decode('utf-8'))
      body['published_date'] = datetime.datetime.now()
      form = Create_book(body)
      if form.is_valid():
         #book = Book.objects.create(**body)
         book = form.save()
         return HttpResponse({'Book Id is : ', book.id})
      return HttpResponse({'data format is not valid;'})


def index(request):
    books= Book.objects.all()
    return render(request, 'books.html', context={"books":books})
   
def get_all_book(request):
    books = list(Book.objects.all().values())
    return JsonResponse(books , safe=False)


def display_books(request):
  books = Book.objects.all().values()
  template = loader.get_template('All_books.html')
  context = {
    'mybook': books,
    
  }
  return HttpResponse(template.render(context, request))

