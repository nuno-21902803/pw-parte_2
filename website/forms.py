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
                                                                                            '__/__/____'}),
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
            'opinion_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '⚠️ Atenção: A crítica que vai fazer, tem de ser construtiva e tem de ter bases, no qual se baseou para a escrever, para que num futuro possamos melhorar o site. Obrigado.'}),
            'opinion2': forms.NumberInput(attrs={'type': 'range', 'step': '1', 'max': 10}),
            'opinion3': forms.NumberInput(attrs={'type': 'range', 'step': '1', 'max': 10}),
        }

    # texto a exibir junto à janela de inserção
        labels = {
            'opinion_text': 'Critica',
            'opinion2': 'De 0-10 quão certa é que acha que a informação do site é?',
            'opinion3': 'De 0-10 qual a probabilidade de recomendar o site a um amigo seu?',
        }

#CRIAR O FORM PARA O QUIZZ ---