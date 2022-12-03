from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def HomePage(request):
    return render(request, template_name='Homepage.html')


def QuestionPage(request):
    return render(request, template_name='Questionpage.html')


def ResultPage(request):
    return render(request, template_name='Resultpage.html')


def RankingPage(request):
    return render(request, template_name='Rankingpage.html')

