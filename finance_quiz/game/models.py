from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    ip = models.CharField(max_length=39)


class Question(models.Model):
    statement = models.CharField(max_length=1000)
    options = models.ForeignKey('Options', on_delete=models.CASCADE)
    accuracy = models.FloatField()


class Ranking(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    score = models.SmallIntegerField()


class Options(models.Model):
    option = models.CharField(max_length=200)
    right_option = models.CharField(max_length=1)
