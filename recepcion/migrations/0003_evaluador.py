# Generated by Django 2.1.2 on 2018-10-28 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0002_delete_evaluador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluador',
            fields=[
                ('idEvaluador', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('letra', models.CharField(max_length=1)),
            ],
        ),
    ]
