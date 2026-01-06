from rest_framework import serializers
from book.models import Book
import datetime



class BookSerializer(serializers.ModelSerializer):


    def to_internal_value(self, data):
        data['published_date']= datetime.datetime.now().date()
        data =  super().to_internal_value(data)
        print(data)
        return data

    def to_representation(self, instance):
        response = super().to_representation(instance= instance)
        return response
    

    class Meta:
        model = Book
        fields = "__all__"
        



    
