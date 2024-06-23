from django.views.generic import TemplateView,ListView
from appStock.models import Profesor
from appStock.forms import *

class ProfesorListView(ListView):
    model = Profesor
    template_name = 'profesor/profesor_lst.html'

    def get_context_data(seld,**kwargs):
        context = super().get_context_data(**kwargs)
        context ['titulo'] = 'Listado de Profesores'
        return context