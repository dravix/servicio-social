# Generated by Django 3.2.6 on 2021-09-24 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_publicaciones_respuestas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuestas',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='respuestas',
            name='publicacion',
        ),
        migrations.DeleteModel(
            name='Estudiantes',
        ),
        migrations.DeleteModel(
            name='Programa',
        ),
        migrations.DeleteModel(
            name='Publicaciones',
        ),
        migrations.DeleteModel(
            name='Respuestas',
        ),
    ]
