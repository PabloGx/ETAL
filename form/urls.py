from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_aluno,name='form_aluno'),
]