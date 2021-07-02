from django import forms
from django.forms import ModelForm
from .models import *


class UserDForm(ModelForm):
    class Meta:
        model = User_details
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apelido'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'date_Of_Birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Data no formato : '
                                                                                            'dd/mm/yyyy'}),
            'phone': forms.NumberInput(attrs={'min': 1000}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'name': 'Nome',
            'last_name': 'Apelido',
            'email': 'Email',
            'date_Of_Birth': 'Data Nascimento',
            'phone': 'Telefone',
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'phone': 'Maximo 9 dígitos',
        }


class UserOpinionForm(ModelForm):
    class Meta:
        model = User_Opinion
        fields = '__all__'
        exclude = ['id_user']
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'opinion_text': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': '⚠️ Atenção: A crítica '
                                                                  'que vai fazer, tem de ser '
                                                                  'construtiva. Obrigado.'}),
            'opinion2': forms.NumberInput(attrs={'type': 'range', 'step': '1', 'max': 10}),
            'opinion3': forms.NumberInput(attrs={'type': 'range', 'step': '1', 'max': 10}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'opinion_text': 'Critica',
            'opinion2': 'De 0-10 quão certa é que acha que a informação do site é?',
            'opinion3': 'De 0-10 qual a probabilidade de recomendar o site a um amigo seu?',
        }


# CRIAR O FORM PARA O QUIZZ ---
class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'
        exclude = ['user_id']

        CHOICES_1 = [('reposta1', 'Alan Shearer'), ('reposta2', 'Wayne Rooney'), ('reposta3', 'Sergio Agüero')]
        CHOICES_2 = [('reposta4', 'Sir Alex Ferguson'), ('reposta5', 'Arsene Wenger'), ('reposta6', 'José Mourinho')]
        CHOICES_3 = [('reposta7', 'Gareth Barry'), ('reposta8', 'Frank Lampard'), ('reposta9', 'Ryan Giggs')]
        CHOICES_4 = [('reposta10', 'Wolverhampton'), ('reposta11', 'Norwich City'),
                     ('reposta12', 'Watford Football Club'), ('resposta12', 'Huddersfield Town')]
        CHOICES_5 = [('reposta13', 'Leeds'), ('reposta14', 'Manchester City'),
                     ('reposta15', 'Wolverhampton'), ('resposta16', 'Everton')]
        CHOICES_6 = [('reposta17', 'Gary Neville'), ('reposta18', 'Paul Scholes'), ('reposta19', 'Ryan Giggs')]

        CHOICES_7 = [('reposta20', 'Celtic'), ('reposta21', 'Rangers'), ('reposta22', 'Aberdeen')]

        CHOICES_8 = [('reposta23', 'Kris Boyd'), ('reposta24', 'Henrik Larsson'), ('reposta25', 'Scott McDonald')]

        widgets = {
            'question1': forms.RadioSelect(choices=CHOICES_1),
            'question2': forms.RadioSelect(choices=CHOICES_2),
            'question3': forms.RadioSelect(choices=CHOICES_3),
            'question4': forms.RadioSelect(choices=CHOICES_4),
            'question5': forms.RadioSelect(choices=CHOICES_5),
            'question6': forms.RadioSelect(choices=CHOICES_6),
            'question7': forms.NumberInput(attrs={'type': 'range', 'step': '1', 'max': 5}),
            'question8': forms.RadioSelect(choices=CHOICES_7),
            'question9': forms.RadioSelect(choices=CHOICES_8),
            'question10': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reposta'}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'question1': 'Qual foi o melhor marcador de todos os tempos da Premier League?',
            'question2': 'Quem foi o treinador a ganhar mais títulos na Premier League?',
            'question3': 'Qual foi o jogador que jogo mais partidas na história da Premier League?',
            'question4': 'Que clubes atuaram na Premier League na temporada 2020/2021:',
            'question5': 'Qual destes clubes nunca desceu de divisão na Premier League?',
            'question6': 'Qual foi é o o jogador com mais titulos ganhos na Premier League?',
            'question7': 'Qual destes clubes ganhou mais titulos na Scottish Premier League?',
            'question8': 'Ao serviço do Man United, quantas bolas de ouro (de 0 a 5) ganhou o Ronaldo?:',
            'question9': 'Qual foi o melhor marcador de todos os tempos da Scottish Premier League?',
            'question10': 'Qual o clube Escocês com mais titulos na Scottish Premier League?',
        }
