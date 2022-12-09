from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    fingerprint = models.CharField(max_length=100, unique=True)
    temporary_questions = models.CharField(max_length=50, default='0|0')


class Question(models.Model):
    statement = models.CharField(max_length=1000)
    options = models.CharField(max_length=1000)
    right_option = models.CharField(max_length=1000)
    accuracy = models.FloatField()


class Ranking(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    score = models.SmallIntegerField()

