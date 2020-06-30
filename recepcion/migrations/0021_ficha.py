# Generated by Django 2.1.2 on 2018-11-05 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0020_agenda_asistencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('idFicha', models.AutoField(primary_key=True, serialize=False)),
                ('ap', models.CharField(max_length=11)),
                ('dui', models.CharField(max_length=10)),
                ('fechaFicha', models.DateField(auto_now=True)),
                ('observaciones', models.TextField(max_length=240)),
                ('facturado', models.BooleanField(default=False)),
                ('idEvaluador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recepcion.Evaluador')),
                ('idProgramado', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recepcion.Agenda')),
                ('idResultado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recepcion.TipoResultado')),
            ],
        ),
    ]
