

from django.urls import path
from book.views import current_datetime, current_datetime2,display_books


urlpatterns = [
    path('book-view/', current_datetime),
    path('book-view2/', current_datetime2),
    path('display-book/', display_books),

    
]
