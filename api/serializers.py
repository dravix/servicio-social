from rest_framework import serializers
from .models import Asesor, User, Estudiantes, Programa, Publicaciones, Respuestas

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class EstudiantesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estudiantes
        fields = ['nombre', 'apellidos', 'matricula', 'correo', 'telefono', 'estatus']

class ProgramasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programa
        fields = ['nombre', 'periodo', 'tipo', 'asesor']

class AsesoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asesor
        fields = ['nombre', 'apellido', 'correo', 'estatus']


class PublicacionesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publicaciones
        fields = ['titulo' ,'programa', 'autor', 'fecha', 'contenido']
                                