# Generated by Django 5.0.6 on 2024-06-22 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appStock', '0019_alter_asignatura_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='curso',
            table='cursos',
        ),
        migrations.AlterModelTable(
            name='profesor',
            table='profesores',
        ),
    ]