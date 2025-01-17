# Generated by Django 3.2.9 on 2021-11-21 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('cooking_time', models.CharField(max_length=10, verbose_name='Tiempo de cocción')),
                ('tags', models.CharField(max_length=30, verbose_name='Etiquetas')),
                ('day_time', models.CharField(choices=[('LN', 'Almuerzo'), ('DN', 'Cena'), ('DL', 'Almuerzo/Cena')], default='BR', max_length=2, verbose_name='Momento del día')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(verbose_name='Cantidad')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ingredients', to='schedule.ingredient', verbose_name='Ingrediente')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.meal', verbose_name='Comida')),
            ],
        ),
    ]
