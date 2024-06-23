from django.db import models

# Create your models here.

class Deposito(models.Model):
    name = models.CharField(max_length=40)
    direccion = models.CharField(max_length=70)
    telefono = models.CharField(max_length=20)
    encargado = models.CharField(max_length=80)

    class Meta:
        db_table = "depositos"

    def __str__(self):
        return self.name

class Categoria(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        db_table = "categorias"
    
    def __str__(self):
        return self.name
    
class Mercaderia(models.Model):
    codigo = models.CharField(max_length=15)
    nombre = models.CharField(max_length=80)
    prec_compra = models.IntegerField()
    prec_venta = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        db_table = "mercaderias"
        unique_together = (('id', 'codigo'),)

    def __str__(self):
        return self.nombre
    
class Profesor(models.Model):
    name = models.CharField(max_length=40)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    especialidad = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()

    class Meta:
        db_table = "profesores"

    def __str__(self):
        return f'{self.name} {self.apellido}'


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    profesor = models.CharField(max_length=100)
    duracion = models.PositiveIntegerField()  # Duración en semanas, por ejemplo
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        db_table = "cursos"
        
    def __str__(self):
        return self.nombre
    

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    profesor = models.CharField(max_length=100)
    creditos = models.PositiveIntegerField()
    horario = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        db_table = "asignaturas"

    def __str__(self):
        return self.nombre

    
class Horario(models.Model):
    asignatura = models.CharField(max_length=100)
    profesor = models.CharField(max_length=100)
    dia = models.CharField(max_length=50)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        db_table = "horarios"

    def __str__(self):
        return f'{self.asignatura} - {self.profesor} ({self.dia})'
    

class Asistencia(models.Model):
    estudiante = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
    presente = models.BooleanField(default=False)

    class Meta:
        db_table = "asistencias"

    def __str__(self):
        return f"{self.estudiante} - {'Presente' if self.presente else 'Ausente'}"
    
class Calificacion(models.Model):
    estudiante = models.CharField(max_length=100)
    materia = models.CharField(max_length=100)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "calificaciones"

    def __str__(self):
        return f"{self.estudiante} - {self.materia} - {self.calificacion}"