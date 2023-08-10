from django.contrib import admin
from .models import Book, CustomCards

# Register your models here.
admin.site.register(Book)
admin.site.register(CustomCards)