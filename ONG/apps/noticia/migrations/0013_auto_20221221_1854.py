# Generated by Django 3.2.16 on 2022-12-21 21:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0012_auto_20221219_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2022, 12, 21, 21, 54, 45, 834921, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2022, 12, 21, 21, 54, 45, 833924, tzinfo=utc)),
        ),
    ]
