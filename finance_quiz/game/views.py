from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def HomePage(request):
    return HttpResponse("Oi")


def QuestionPage(request):
    return HttpResponse("Oi")


def ResultPage(request):
    return HttpResponse("Oi")


def RankingPage(request):
    return HttpResponse("Oi")
