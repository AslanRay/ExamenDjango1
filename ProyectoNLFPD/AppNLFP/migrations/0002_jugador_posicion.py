# Generated by Django 2.1.5 on 2019-02-08 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppNLFP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='posicion',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
