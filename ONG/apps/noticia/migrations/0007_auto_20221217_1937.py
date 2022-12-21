# Generated by Django 3.2.16 on 2022-12-17 22:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noticia', '0006_alter_noticias_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2022, 12, 17, 22, 37, 58, 436375, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('texto', models.TextField()),
                ('publicado', models.DateField(default=datetime.datetime(2022, 12, 17, 22, 37, 58, 436375, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('noticia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='noticia.noticias')),
            ],
            options={
                'verbose_name': 'noticia',
                'verbose_name_plural': 'noticias',
                'ordering': ['-publicado'],
            },
        ),
    ]
