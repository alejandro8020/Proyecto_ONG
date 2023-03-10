# Generated by Django 4.1.4 on 2022-12-14 20:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('introduccion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('texto', models.TextField()),
                ('activo', models.BooleanField(default=True)),
                ('imagen', models.ImageField(blank=True, default='noticia/default.png', upload_to='actividad')),
                ('publicado', models.DateField(default=datetime.datetime(2022, 12, 14, 20, 56, 47, 784684, tzinfo=datetime.timezone.utc))),
            ],
            options={
                'verbose_name': 'actividad',
                'verbose_name_plural': 'actividades',
                'ordering': ['-publicado'],
            },
        ),
    ]
