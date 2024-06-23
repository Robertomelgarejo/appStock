from django.contrib import admin
from . models import *

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class DepositoAdmin(admin.ModelAdmin):
    list_display = ['id','name','direccion', 'telefono', 'encargado']

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['id','name','apellido','email','especialidad','fecha_contratacion']
    search_fields= ['name', 'apellido', 'email', 'especialidad']


class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'profesor', 'duracion', 'fecha_inicio', 'fecha_fin')
    search_fields = ('nombre', 'profesor')
    list_filter = ('fecha_inicio', 'fecha_fin')

class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'profesor', 'creditos', 'horario', 'fecha_inicio', 'fecha_fin')
    search_fields = ('nombre', 'profesor')
    list_filter = ('fecha_inicio', 'fecha_fin')

class HorarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'asignatura', 'profesor', 'dia', 'hora_inicio', 'hora_fin')
    search_fields = ('asignatura', 'profesor', 'dia')
    list_filter = ('dia', 'hora_inicio', 'hora_fin')

class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'estudiante', 'fecha', 'presente')
    search_fields = ('estudiante', 'fecha')
    list_filter = ('fecha', 'presente')

class CalificacionAdmin(admin.ModelAdmin):
    list_display = ['id', 'estudiante', 'materia', 'calificacion', 'fecha']
    search_fields = ['estudiante', 'materia']
    list_filter = ['fecha']

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Deposito, DepositoAdmin)
admin.site.register(Profesor,ProfesorAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Asignatura, AsignaturaAdmin)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Asistencia, AsistenciaAdmin)
admin.site.register(Calificacion, CalificacionAdmin)