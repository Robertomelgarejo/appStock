# Generated by Django 5.0.6 on 2024-06-19 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appStock', '0017_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='profesor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='curso',
            name='profesor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterModelTable(
            name='asignatura',
            table=None,
        ),
        migrations.AlterModelTable(
            name='curso',
            table=None,
        ),
        migrations.AlterModelTable(
            name='profesor',
            table=None,
        ),
    ]