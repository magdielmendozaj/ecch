# Generated by Django 5.0.2 on 2024-02-21 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educativeoffer', '0002_alter_localidad_codigopostal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telefono',
            name='telefono',
            field=models.BigIntegerField(unique=True),
        ),
    ]
