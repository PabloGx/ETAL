from django import forms
from .models import Aluno

class Alunoform(forms.ModelForm):
    LISTA_SEXO = [
    ('Masculino','Masculino'),
    ('Feminino','Feminino'),
]

    ESCOLHAS_MINI_CURSO = [
    ('Introdução a computação gráfica','Introdução a computação gráfica'),
    ('Introdução a computação gráfica','Introdução a Construção de jogos'),
    ('Introdução a computação gráfica','Minicurso de Realidade Virtual'),
    ('Introdução a computação gráfica','Computação nas Nuvens'),
]
    ESCOLHAS_CURSO = [
    ('Informática','Informática'),
    ('Alimentos','Alimentos'),
    ('Apicultura','Apicultura'),
]

    sexo = forms.ChoiceField(
        choices=LISTA_SEXO,
        widget= forms.RadioSelect()
    )

    curso = forms.ChoiceField(
        choices= ESCOLHAS_CURSO
        
    )

    mini_curso = forms.ChoiceField(
        choices= ESCOLHAS_MINI_CURSO,
        widget=forms.CheckboxSelectMultiple()
        
    )
    
    class Meta:
        model = Aluno
        fields= '__all__'

    