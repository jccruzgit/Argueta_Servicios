# Generated by Django 2.1.2 on 2018-11-03 07:49

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0006_auto_20181103_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='idEmpresa',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='idPersona', chained_model_field='persona', on_delete=django.db.models.deletion.CASCADE, to='recepcion.Empresa'),
        ),
    ]