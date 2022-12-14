from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import QuestionForm, UserForm
from game.models import User, Ranking

from game.utils import fingerprint_generator

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
            try:
                User.objects.get(fingerprint=request.session['fingerprint'])
            except:
                fingerprint = fingerprint_generator()

                user = User(
                    name=form.cleaned_data['name'],
                    email=form.cleaned_data['email'],
                    fingerprint=fingerprint,
                    temporary_questions='0|0|0'
                )
                user.save()

                request.session['fingerprint'] = fingerprint

            return HttpResponseRedirect('/question')
        else:
            return HttpResponse(f'{form.errors}')


def QuestionPage(request):
    try:
        user = User.objects.get(fingerprint=request.session['fingerprint'])
    except:
        return HttpResponseRedirect('/homepage')

    form = QuestionForm()
    if request.method == 'GET':
        return render(request, template_name='Questionpage.html', context={
            'form': form,
            'username': user.name
        })
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            if not ('|' in user.temporary_questions):
                user.temporary_questions = '0|0|0'
            # ultima questão correta ou não | total de questões corretas | total de questões
            q = user.temporary_questions.split('|')

            if form.right_choice == form['opcoes'].value():
                print(form.right_choice, form['opcoes'].value())
                q[0] = '1'
                q[1] = int(q[1]) + 1
            else:
                q[0] = '0'
            q[2] = int(q[2]) + 1
            user.temporary_questions = f'{q[0]}|{q[1]}|{q[2]}'
            user.save()

            if q[2] == 10:
                return HttpResponseRedirect('/results')
            else:
                return HttpResponseRedirect('/resultquestion')


def ResultQuestionPage(request):
    try:
        user = User.objects.get(fingerprint=request.session['fingerprint'])
    except:
        return HttpResponseRedirect('/homepage')

    q = user.temporary_questions.split('|')
    return render(request, template_name='ResultQuestionPage.html', context={
        'answer': q[0]
    })


def ResultPage(request):
    try:
        user = User.objects.get(fingerprint=request.session['fingerprint'])
    except:
        return HttpResponseRedirect('/homepage')

    q = user.temporary_questions.split('|')

    if int(q[2]) < 10:
        return HttpResponseRedirect('/question')

    ranking = Ranking(
        user=user,
        score=q[1]
    )
    ranking.save()

    user.fingerprint = fingerprint_generator()
    user.temporary_questions = ''
    user.save()

    return render(request, template_name='Resultspage.html', context={
        'correct_amount': ranking.score
    })


def RankingPage(request):
    raking = Ranking.objects.all().order_by('-score')

    return render(request, template_name='Rankingpage.html', context={
        'ranking': raking
    })

