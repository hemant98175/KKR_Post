from django.db import models


class Questions(models.Model):

    q_number = models.AutoField(primary_key=True)
    user = models.CharField(max_length=122)
    question = models.TextField()
    date = models.DateField()
# Create your models here.

class Answere(models.Model):
    q_number = models.CharField(max_length=122)
    user = models.CharField(max_length=122)
    answere = models.TextField()
    date = models.DateField()
