# Generated by Django 3.2.16 on 2022-12-18 15:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0005_alter_eventos_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2022, 12, 18, 15, 10, 31, 823164, tzinfo=utc)),
        ),
    ]
