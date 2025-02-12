# Generated by Django 5.0.6 on 2024-06-18 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appStock', '0016_delete_horario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignatura', models.CharField(max_length=100)),
                ('profesor', models.CharField(max_length=100)),
                ('dia', models.CharField(max_length=50)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
            ],
            options={
                'db_table': 'horarios',
            },
        ),
    ]
