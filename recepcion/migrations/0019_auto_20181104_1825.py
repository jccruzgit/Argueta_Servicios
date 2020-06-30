# Generated by Django 2.1.2 on 2018-11-05 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0018_auto_20181103_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='idPersona',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='persona',
        ),
        migrations.AddField(
            model_name='empresa',
            name='persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recepcion.Persona'),
        ),
    ]