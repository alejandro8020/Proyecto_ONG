# Generated by Django 3.2.16 on 2022-12-15 01:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('actividad', '0009_alter_actividad_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2022, 12, 15, 1, 33, 7, 570341, tzinfo=utc)),
        ),
    ]
