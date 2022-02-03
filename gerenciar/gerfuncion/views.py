from django.shortcuts import render
from django.views.generic import ListView

from gerenciar.gerenciar.models import Funcionario

class ListaFuncionarios(ListView):
    template_name = "templates/funcionarios.html"
    model = Funcionario
    context_object_name ="funcionarios"




# Create your views here.
