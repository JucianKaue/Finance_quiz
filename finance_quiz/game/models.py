from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)

    ip = models.CharField(max_length=39, unique=True)

class Question(models.Model):
    statement = models.CharField(max_length=1000)
    options = models.CharField(max_length=1000)
    right_option = models.CharField(max_length=1000)
    accuracy = models.FloatField()


class Ranking(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    score = models.SmallIntegerField()

