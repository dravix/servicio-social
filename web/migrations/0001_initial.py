# Generated by Django 3.2.6 on 2021-09-06 23:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('folio', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('periodo', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=200)),
                ('asesor', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('matricula', models.IntegerField()),
                ('correo', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('foto', models.CharField(max_length=200)),
                ('estatus', models.CharField(max_length=200)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.programa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
