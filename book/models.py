from django.db import models
from datetime import datetime

# Create your models here.
class Book(models.Model):
    CATEGORY_CHOICE=[
        ("Fun", "Fun"),
        ("SC", "Science"),
        ("HC", "Historical"),

    ]



    name = models.CharField(max_length=50 , null=True)
    published_date = models.DateField(default=datetime.now)
    price = models.FloatField()
    category = models.CharField(max_length=3 , choices=CATEGORY_CHOICE)

    def __str__(self):
        return self.name
