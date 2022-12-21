# Generated by Django 3.2.16 on 2022-12-17 22:45

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0007_auto_20221217_1937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentarios',
            options={'ordering': ['-publicado'], 'verbose_name': 'comentario', 'verbose_name_plural': 'comentarios'},
        ),
        migrations.AddField(
            model_name='comentarios',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='noticia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='noticia.noticias'),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2022, 12, 17, 22, 45, 22, 6346, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2022, 12, 17, 22, 45, 22, 6346, tzinfo=utc)),
        ),
    ]
