from django import forms
from game.models import User, Question

from random import randint, shuffle


class QuestionForm(forms.Form):
    q = Question.objects.get(id=randint(1, (len(Question.objects.all())+1)))

    opt = q.options.split('>-<')                # Splits the string having the choices in a list
    n_opt = [i for i in range(0, len(opt))]     # Generate a number list from 0 to the number of options
    shuffle(n_opt)                              # Reorganize de number list in a pseudo-aleatory sequence
    
    choices = []
    for i in n_opt:
        choices.append(
            (f'{opt[i]}', f'{opt[i]}')
        )

    question = q.statement
    print(q.right_option)
    right_choice = q.right_option
    opcoes = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']
