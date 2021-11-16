# Generated by Django 3.2.6 on 2021-11-16 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0003_auto_20210924_0630'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=200)),
                ('foto', models.CharField(max_length=200)),
                ('estatus', models.CharField(max_length=200)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('folio', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('periodo', models.CharField(max_length=200)),
                ('tipo', models.CharField(choices=[('SS', 'Servicio Social'), ('PP', 'Practica Profesional')], max_length=200)),
                ('asesor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='web.asesor')),
            ],
        ),
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('contenido', models.TextField()),
                ('estatus', models.CharField(choices=[('ACTIVO', 'Activo'), ('DESACTIVADO', 'Desactivado'), ('ELIMINADO', 'Eliminado')], max_length=200)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('programa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.programa')),
            ],
        ),
        migrations.CreateModel(
            name='Respuestas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('contenido', models.TextField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.publicaciones')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('matricula', models.IntegerField(unique=True)),
                ('correo', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('foto', models.CharField(max_length=200)),
                ('estatus', models.CharField(choices=[('ACTIVO', 'Activo'), ('DESACTIVADO', 'Desactivado'), ('ELIMINADO', 'Eliminado')], max_length=200)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.programa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]