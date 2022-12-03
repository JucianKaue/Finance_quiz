from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def redirect(request):
    return HttpResponseRedirect("/homepage")

def HomePage(request):
    if request.method == 'GET':
        return render(request, template_name='Homepage.html', context={
            'link_css': 'homepage.css'
        })
    elif request.method == 'POST':
        return HttpResponseRedirect('/question')


def QuestionPage(request):
    return render(request, template_name='Questionpage.html')


def ResultPage(request):
    return render(request, template_name='Resultpage.html')


def RankingPage(request):
    return render(request, template_name='Rankingpage.html')

