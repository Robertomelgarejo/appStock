# Generated by Django 5.0.6 on 2024-05-29 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appStock', '0011_delete_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('profesor', models.CharField(max_length=100)),
                ('duracion', models.PositiveIntegerField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
            ],
        ),
    ]
