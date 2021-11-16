from api.models import Estudiantes
from django.shortcuts import render
from rest_framework import viewsets, permissions

from django.contrib.auth.models import User
from .serializers import AsesoresSerializer, ProgramasSerializer, PublicacionesSerializer, UserSerializer, EstudiantesSerializer
from . import models

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny,]

    def create(self, request, *args, **kwargs):
        request.data['username'] = request.data['matricula']
        return super().create(request, *args, **kwargs)

class EstudiantesViewSet(viewsets.ModelViewSet):
    queryset = models.Estudiantes.objects.all()
    serializer_class = EstudiantesSerializer

class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = models.Programa.objects.all()
    serializer_class = ProgramasSerializer    

class AsesoresViewSet(viewsets.ModelViewSet):
    queryset = models.Asesor.objects.all()
    serializer_class = AsesoresSerializer    

class PublicacionesViewSet(viewsets.ModelViewSet):
    queryset = models.Publicaciones.objects.all()
    serializer_class = PublicacionesSerializer        