# Generated by Django 2.1.2 on 2018-12-28 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0024_ficha_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, null=True),
        ),
    ]