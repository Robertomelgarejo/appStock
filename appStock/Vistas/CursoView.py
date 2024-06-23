from typing import Any
from django.views.generic import TemplateView, ListView
from appStock.models import Curso
from appStock.forms import *

class CursoListView(ListView):
    model = Curso
    template_name = 'cursos/curso_lst.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Cursos'
        return context
    