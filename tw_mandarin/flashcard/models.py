from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    chinese = models.CharField(max_length=225)
    pinyin = models.CharField(max_length=225)
    english = models.CharField(max_length=225)
    book = models.SmallIntegerField(default=None)
    lesson = models.SmallIntegerField(default=None)
    section = models.SmallIntegerField(default=None)

    def __str__(self):
        return f"{self.chinese} : {self.english}"

class CustomCards(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customcards", null=True)

    chinese = models.CharField(max_length=225)
    pinyin = models.CharField(max_length=225)
    english = models.CharField(max_length=225)
    
    def __str__(self):
        return f"{self.chinese} : {self.english}"