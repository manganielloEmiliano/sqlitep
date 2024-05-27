# Generated by Django 4.2.5 on 2023-11-13 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mesa', '0006_mesa_duracion_meses'),
        ('socio', '0003_alter_socio_fecha_nacimiento'),
        ('mensualidad', '0003_remove_mensualidad_fecha_vencimiento_mensualidad_mes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensualidad',
            name='mesa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensualidades', to='mesa.mesa'),
        ),
        migrations.AlterField(
            model_name='mensualidad',
            name='socio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensualidades', to='socio.socio'),
        ),
    ]
