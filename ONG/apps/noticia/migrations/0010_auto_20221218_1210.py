# Generated by Django 3.2.16 on 2022-12-18 15:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0009_auto_20221217_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2022, 12, 18, 15, 10, 31, 819174, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2022, 12, 18, 15, 10, 31, 819174, tzinfo=utc)),
        ),
    ]
