1. Crear una carpeta para el proyecto Django

    `mkdir 87744-django-ejercicios`

2. Acceder al proyecto

    `cd 87744-django-ejercicios`

3. Inicializar proyecto Python
    
    `uv init --no-package`

4. Crear entorno virtual

    `uv venv`

5. Activar entorno virtual
    
    Windows: `.venv\Scripts\activate`
    
    Linux o Mac: `source/bin/activate`

6. Instalar django
    
    `uv add django`

7. Crear proyecto django

    `mkdir src`

    `cd src`

    `django-admin startproject config .`

8. Iniciar servidor django
       
    `python manage.py runserver`

9. Crear aplicación django "core"

    `python manage.py startapp core`

10. Registrar la nueva aplicación Django en INSTALLED_APPS del módulo "config.settings" 