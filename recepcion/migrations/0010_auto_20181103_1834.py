# Generated by Django 2.1.2 on 2018-11-04 00:34

from django.db import migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0009_auto_20181103_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='idEmpresa',
            field=smart_selects.db_fields.ChainedManyToManyField(to='recepcion.Empresa'),
        ),
    ]
