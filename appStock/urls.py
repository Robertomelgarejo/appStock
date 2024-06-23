from django.urls import path
from appStock.Vistas.HomeView import *
from appStock.Vistas.DepositoView import *
from appStock.Vistas.Profesorview import *
from appStock.Vistas.CursoView import *
from appStock.Vistas.AsignaturaView import *
from appStock.Vistas.HorarioView import *
from appStock.Vistas.AsistenciaView import *
from appStock.Vistas.CalificacionView import *

urlpatterns = [
    path('', HomeView.as_view(), name="index"),
    path('deposito/', DepositoListView.as_view(), name='deposito_lst'),
    path('profesor/', ProfesorListView.as_view(), name='profesor_lst'),
    path('cursos/', CursoListView.as_view(), name='curso_lst'),
    path('asignatura/', AsignaturaListView.as_view(), name='asignatura_lst'),
    path('asignatura/crear/', AsignaturaCreateView.as_view(), name='crear_asignatura'),
    path('asignatura/editar/<int:id>/', AsignaturaUpdateView.as_view(), name='editar_asignatura'),
    path('asignatura/eliminar/<int:id>/', AsignaturaDeleteView.as_view(), name='eliminar_asignatura'),
    path('horario/', HorarioListView.as_view(), name='horario_lst'),
    path('asistencia/', AsistenciaListView.as_view(), name='asistencia_lst'),
    path('calificaciones/', CalificacionListView.as_view(), name='calificacion_lst'),

]