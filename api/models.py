from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, DO_NOTHING

class Asesor(models.Model):
    usuario =  models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    foto = models.CharField(max_length=200)
    estatus = models.CharField(max_length=200)

class Programa(models.Model):
    TIPOS = [
        ('SS', "Servicio Social"),
        ('PP', "Practica Profesional")
    ]
    folio =  models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=200)
    periodo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200, choices=TIPOS)
    asesor = models.ForeignKey(Asesor, on_delete=DO_NOTHING)



class Estudiantes(models.Model):
    ESTATUS = [
        ("ACTIVO","Activo"),
        ("DESACTIVADO","Desactivado"),
        ("ELIMINADO","Eliminado"),

    ]    
    usuario =  models.ForeignKey(User, on_delete=models.CASCADE)
    folio =  models.ForeignKey(Programa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    matricula =  models.IntegerField(unique=True)
    correo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    foto = models.CharField(max_length=200)
    estatus = models.CharField(max_length=200, choices=ESTATUS)

class Publicaciones(models.Model):
    ESTATUS = [
        ("ACTIVO","Activo"),
        ("DESACTIVADO","Desactivado"),
        ("ELIMINADO","Eliminado"),

    ]
    programa = models.ForeignKey(Programa, on_delete=CASCADE)
    titulo = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User,on_delete=CASCADE)
    contenido = models.TextField()
    estatus = models.CharField(max_length=200,choices=ESTATUS)

class Respuestas(models.Model):
    publicacion = models.ForeignKey(Publicaciones, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    fecha = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()