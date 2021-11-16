from django.urls import path,  include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'estudiantes', views.EstudiantesViewSet)
router.register(r'programa', views.ProgramaViewSet)
router.register(r'publicaciones', views.PublicacionesViewSet)


urlpatterns = [
    path('', include(router.urls)) ,
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
