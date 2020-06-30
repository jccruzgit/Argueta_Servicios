# Generated by Django 2.1.2 on 2018-11-04 02:19

from django.db import migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0015_auto_20181103_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='idEmpresa',
        ),
        migrations.AddField(
            model_name='agenda',
            name='idEmpresa',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_field='idPersona', chained_model_field='persona', to='recepcion.Empresa'),
        ),
    ]
