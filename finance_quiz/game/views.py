from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import QuestionForm, UserForm
from game.models import User, Ranking

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
                ip=request.META.get('REMOTE_ADDR'),
                temporary_questions='0|0|0'
            )
            user.save()
            return HttpResponseRedirect('/question')
        else:
            return HttpResponse(f'{form.errors}')


def QuestionPage(request):
    form = QuestionForm()
    user = User.objects.get(ip=request.META.get('REMOTE_ADDR'))
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
    user = User.objects.get(ip=request.META.get('REMOTE_ADDR'))
    q = user.temporary_questions.split('|')
    return render(request, template_name='ResultQuestionPage.html', context={
        'answer': q[0]
    })


def ResultPage(request):
    user = User.objects.get(ip=request.META.get('REMOTE_ADDR'))
    q = user.temporary_questions.split('|')

    if int(q[2]) < 10:
        return HttpResponseRedirect('/question')

    ranking = Ranking(
        user=user,
        score=q[1]
    )
    ranking.save()

    user.ip = ''
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

