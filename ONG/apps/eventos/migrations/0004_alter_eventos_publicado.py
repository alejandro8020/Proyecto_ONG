# Generated by Django 4.1.4 on 2022-12-17 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_alter_eventos_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2022, 12, 17, 17, 7, 8, 769443, tzinfo=datetime.timezone.utc)),
        ),
    ]
