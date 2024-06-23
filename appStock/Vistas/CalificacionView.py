from django.views.generic import TemplateView, ListView
from appStock.models import Calificacion
from appStock.forms import *

class CalificacionListView(ListView):
    model = Calificacion
    template_name = 'calificacion/calificacion_lst.html'
    context_object_name = 'calificaciones'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Calificaciones'
        return context