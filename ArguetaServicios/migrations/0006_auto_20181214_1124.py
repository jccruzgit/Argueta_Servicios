# Generated by Django 2.1.2 on 2018-12-14 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArguetaServicios', '0005_auto_20181214_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precio',
            name='precio',
            field=models.IntegerField(),
        ),
    ]