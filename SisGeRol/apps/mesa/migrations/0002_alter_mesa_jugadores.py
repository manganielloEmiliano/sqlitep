# Generated by Django 4.2.5 on 2023-09-12 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socio', '0002_socio_apellido_socio_dni_socio_fecha_nacimiento_and_more'),
        ('mesa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesa',
            name='jugadores',
            field=models.ManyToManyField(blank=True, related_name='mesas_jugadas', to='socio.socio'),
        ),
    ]
