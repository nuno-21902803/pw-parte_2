from django import forms
from django.forms import ModelForm, SelectDateWidget
from django.utils.datetime_safe import datetime

from .models import User_details


class UserDForm(ModelForm):
    class Meta:
        model = User_details
        fields = '__all__'

        date_Of_Birth = forms.DateField(input_formats=['%d %m %Y'], widget=SelectDateWidget, initial=datetime.today())
    # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apelido'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.NumberInput(),
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