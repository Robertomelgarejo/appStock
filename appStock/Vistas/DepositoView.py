from django.views.generic import TemplateView, ListView
from appStock.models import Deposito
from appStock.forms import *


class DepositoListView(ListView):
    model = Deposito
    template_name = 'deposito/deposito_lst.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Alumnos'
        return context

