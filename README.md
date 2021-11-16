# Poyecto Groupware para Servicio Social y Practica Profesional

Este procyeto esta disenado para ayudar a los participantes en el proceso de servicio social y practica profesional para agilizar el registro y la comunicacion entre el prestador de servicios y el asesor.

## Sobre el proyecto

Este proyecto esta basado en Django como framework de desarrollo y se utilizan base de datos relacionales usando el ORM provisto por Django asi que se puede utilizar sqlite como base de datos de pruebas aunque se recomienda cambiar los parametros de la base de datos para usarse en produccion.

## Requisitos:




### Instalaci&oacute;on

Una vez configurada la Base de Datos (o dejar como esta para utilizar con SQLite) es necesario instalar las dependencias de python.
Los pasos para poder servir este proyecto son:

* Instalar :snake: Python 3.8+ .


* Instalar [Entornos virtuales](https://docs.python-guide.org/dev/virtualenvs/)
    Se recomienda usar un entorno virtual para aislar las dependencias que usa python.
    * Crear entorno virtual 
        ```
        pip install virtualenv
        virtualenv venv
        ```
    * Usar entorno
        Esto activara el entorno virtual, una vez en este modo todo lo que se instale se almacenara en el directorio venv

        ```
        source venv/bin/activate
        ```
    * Instalar dependencias
        ```
        pip install -r requirements.txt
        ```

* Iniciar la base de datos
    La base de datos se puede iniciar corriendo las migraciones 
    ```
    python manage.py migrate
    ```
    Esto ejecutara los comandos de SQL necesario es la base de datos para tener una estructura inicial

* Servir proyecto
    En este paso el proyecto esta listo para ser servido, para utilizarlo en modo desarrollo en neceario usar django manager de la siguiente manerra:
    ```
    python manage.py runserver
    ```



