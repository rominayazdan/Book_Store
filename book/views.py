from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
import datetime
from django.template import loader
from book.models import Book
from django.views.decorators.csrf import csrf_exempt
from book.forms import Create_book
from rest_framework.views import APIView
from book.serializers import BookSerializer
from rest_framework import generics






def current_datetime(request):
    print('request method is', request.method)
    #now = datetime.datetime.now()
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
         return JsonResponse({'Book_id': book.id}, safe=False)
      return JsonResponse({'data format is not valid;'})

   elif request.method == "GET":
      books = list(Book.objects.all().values())
      return JsonResponse(books , safe=False)




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

class BookAPI(APIView):
   
   def post(self, request):
      body = json.loads(request.body.decode('utf-8'))
      body['published_date'] = datetime.datetime.now().date()
      form = BookSerializer(data=body)
      #print('body', body)
      if form.is_valid():
         book = form.save()
         return JsonResponse({'Book_id': book.id})
      return JsonResponse({'error': 'data format is not valid'})
   
   def get(self, request):
      books = list(Book.objects.all().values())
      return JsonResponse(books , safe=False)

       





class BookGenericAPI(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class GetBookAPI(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class DeleteBookAPI(generics.DestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class UpdateBookAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    


