# Generated by Django 2.1.2 on 2018-11-03 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0005_agenda_idpersona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='idPersona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recepcion.Persona'),
        ),
    ]
