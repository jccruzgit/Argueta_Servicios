# Generated by Django 2.1.2 on 2018-12-28 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0023_auto_20181105_1458'),
        ('ArguetaServicios', '0006_auto_20181214_1124'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='precio',
            unique_together={('idEmpresa', 'idTipoPrueba')},
        ),
    ]
