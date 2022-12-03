from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import QuestionForm

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
    form = QuestionForm()

    if request.method == 'GET':
        return render(request, template_name='Questionpage.html', context={
            'form': form
        })
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            if form.right_choice[0] == form['opcoes'].value():
                return HttpResponse(f"CERTO! {form['opcoes'].value()} {form.right_choice[0]}")
            else:
                return HttpResponse(f"ERRADO! {form['opcoes'].value()} {form.right_choice[0]}")


def ResultPage(request):
    return render(request, template_name='Resultpage.html')


def RankingPage(request):
    return render(request, template_name='Rankingpage.html')

