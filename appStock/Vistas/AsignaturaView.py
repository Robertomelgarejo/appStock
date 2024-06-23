import json
from django.views.generic import TemplateView, ListView
from appStock.models import Asignatura
from appStock.forms import AsignaturaForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View

class AsignaturaListView(ListView):
    model = Asignatura
    template_name = 'asignatura/asignatura_lst.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Materias'
        return context

@method_decorator(csrf_exempt, name='dispatch')
class AsignaturaCreateView(View):
    def post(self, request):
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

@method_decorator(csrf_exempt, name='dispatch')
class AsignaturaUpdateView(View):
    def post(self, request, id):
        asignatura = get_object_or_404(Asignatura, id=id)
        form = AsignaturaForm(request.POST, instance=asignatura)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

@method_decorator(csrf_exempt, name='dispatch')
class AsignaturaDeleteView(View):
    def post(self, request, id):
        asignatura = get_object_or_404(Asignatura, id=id)
        asignatura.delete()
        return JsonResponse({'success': True})
