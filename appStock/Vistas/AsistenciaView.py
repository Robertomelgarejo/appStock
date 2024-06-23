from django.views.generic import TemplateView, ListView
from appStock.models import Asistencia
from appStock.forms import *

class AsistenciaListView(ListView):
    model = Asistencia
    template_name = 'asistencia/asistencia_lst.html'
    context_object_name = 'asistencias'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Asistencias'
        return context