# Generated by Django 2.1.2 on 2018-11-04 01:33

from django.db import migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0010_auto_20181103_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='idEmpresa',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_field='idPersona', chained_model_field='persona', to='recepcion.Empresa'),
        ),
    ]