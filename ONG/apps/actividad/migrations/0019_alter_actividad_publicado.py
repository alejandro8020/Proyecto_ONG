# Generated by Django 3.2.16 on 2022-12-18 15:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('actividad', '0018_alter_actividad_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2022, 12, 18, 15, 51, 22, 256297, tzinfo=utc)),
        ),
    ]
