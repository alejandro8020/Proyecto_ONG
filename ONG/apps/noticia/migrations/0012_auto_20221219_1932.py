# Generated by Django 3.2.16 on 2022-12-19 22:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0011_auto_20221218_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2022, 12, 19, 22, 32, 33, 763878, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2022, 12, 19, 22, 32, 33, 762880, tzinfo=utc)),
        ),
    ]
