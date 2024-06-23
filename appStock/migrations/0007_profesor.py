# Generated by Django 5.0.6 on 2024-05-29 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appStock', '0006_delete_alumno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('especialidad', models.CharField(max_length=100)),
                ('fecha_contratacion', models.DateField()),
            ],
        ),
    ]