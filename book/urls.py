

from django.urls import path
from book.views import *


urlpatterns = [
    path('',get_all_book),
    path('book-view/', book_view),

    path('index/', index),
    path('display-book/', display_books),
    path('add/', add_book),

    
]
