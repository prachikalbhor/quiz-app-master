from django.db import models

# Create your models here.
choice_list = [(x,x) for x in range(1,5)]
class Questions(models.Model):
    question = models.CharField(max_length=250)
    a1 = models.CharField(max_length=100)
    a2 = models.CharField(max_length=100)
    a3 = models.CharField(max_length=100)
    a4 = models.CharField(max_length=100)
    right=models.IntegerField(choices=choice_list)
class Review(models.Model):
    name = models.CharField(max_length=100)
    review = models.CharField(max_length=1000) 
    rating = models.IntegerField(default=0)   