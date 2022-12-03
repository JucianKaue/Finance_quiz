from django import forms


class QuestionForm(forms.Form):
    question = 'Uma empresa desconta do salário anual de seus funcionários certa porcentagem para um plano de previdência privada. O desconto é de p% sobre             R$ 28.000,00 de renda anual, mais (p + 2)% sobre o montante anual do salário que excede R$ 28.000,00. João teve desconto total de (p + 0,25)% do seu salário anual para o plano de previdência privada. O salário anual de João, em reais, sem o desconto do plano de previdência é:'
    right_choice = ('B', '32.000,00')
    choices = (
        ('A', '28.000,00'),
        ('B', '32.000,00'),
        ('C', '32.000,00'),
        ('D', '42.000,00'),
        ('E', '56.000,00')
    )
    opcoes = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
