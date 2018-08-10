from django import forms
from skywalker.models import User
from skywalker.models import Turma
from django.forms import ModelForm


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    siap = forms.CharField(
        required = True,
        label = 'Siap',
        max_length = 32,
    )
    nivel = forms.IntegerField(
        required = True,
        label = 'Nivel',
    )
    categoria = forms.CharField(
        required = True,
        label = 'Categoria',
        max_length = 32,
    )
	
    class Meta:
        model = User

class TeamRegistrationForm(forms.Form):
    nome = forms.CharField(
        required = True,
        label = 'Nome',
        max_length = 32
    )
    idioma = forms.CharField(
        required = True,
        label = 'Idioma',
        max_length = 32
    )

    class Meta:
        model = Turma
    
class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class EditTeamForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'idioma']
