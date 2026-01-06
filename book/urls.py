

from django.urls import path
from book.views import *


urlpatterns = [
    path('',get_all_book),
    path('book-view/', book_view),

    path('index/', index),
    path('display-book/', display_books),
    path('add/', add_book),
    path('create/', BookAPI.as_view()),
    path('book-generic/', BookGenericAPI.as_view()),
    path('get-book/<str:pk>', GetBookAPI.as_view()),
    path('delete-book/<str:pk>', DeleteBookAPI.as_view()),
    path('update-book/<str:pk>', UpdateBookAPI.as_view()),

    
]
