from typing import Any
from django.views.generic import TemplateView,ListView
from appStock.models import Horario
from appStock.forms import *

class HorarioListView(ListView):
    model = Horario
    template_name = 'horario/horario_lst.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['titulo'] = 'Listado de Horarios'
        return context