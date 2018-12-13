# Generated by Django 2.1.4 on 2018-12-13 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listacompra', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productosm',
            old_name='imagen_producto',
            new_name='image_producto',
        ),
        migrations.RenameField(
            model_name='productosm',
            old_name='nombre',
            new_name='nombreP',
        ),
        migrations.RenameField(
            model_name='tiendasm',
            old_name='nombre',
            new_name='nombreT',
        ),
        migrations.AlterField(
            model_name='productosm',
            name='costo_presupuestado',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='productosm',
            name='costo_real',
            field=models.PositiveIntegerField(),
        ),
    ]
