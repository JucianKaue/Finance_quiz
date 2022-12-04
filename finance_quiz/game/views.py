from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import QuestionForm, UserForm
from game.models import User

# Create your views here.
def redirect(request):
    return HttpResponseRedirect("/homepage")


def HomePage(request):
    form = UserForm()
    if request.method == 'GET':
        return render(request, template_name='Homepage.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                ip=request.META.get('REMOTE_ADDR')
            )
            user.save()
            return HttpResponseRedirect('/question')
        else:
            return HttpResponse(form.errors)


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

