from django import forms
from .models import *

class DepositoModelForm(forms.ModelForm):
    class Meta:
        model = Deposito
        fields = '__all__'

class ProdesorModelForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

class CursoModelForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'



class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['nombre', 'descripcion', 'profesor', 'creditos', 'horario', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre de la asignatura'}),
            'descripcion': forms.Textarea(attrs={'placeholder': 'Descripción de la asignatura'}),
            'profesor': forms.TextInput(attrs={'placeholder': 'Nombre del profesor'}),
            'creditos': forms.NumberInput(attrs={'placeholder': 'Número de créditos'}),
            'horario': forms.TextInput(attrs={'placeholder': 'Horario'}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get("fecha_inicio")
        fecha_fin = cleaned_data.get("fecha_fin")

        if fecha_inicio and fecha_fin and fecha_inicio > fecha_fin:
            raise forms.ValidationError("La fecha de inicio no puede ser posterior a la fecha de fin.")
        
        
class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        exclude = ['fecha']

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['estudiante', 'materia', 'calificacion']