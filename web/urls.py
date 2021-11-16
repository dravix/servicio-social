from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('registro', views.registro, name='registro'),
    path('login', views.login, name='login'),
    

]
