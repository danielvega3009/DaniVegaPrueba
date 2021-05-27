He creado un proyecto Python con el Framework Django, para ello he creado un entorno virtual,,necesario para dicho framework,
en la carpeta env con "pip install virtualenv" y "python -m venv env" para darle el nombre env a dicho entorno.

Dentro de app tenemos la app principal que enlaza con la aplicación users, que es la aplicación que se ha realizado para
la prueba.
descargar desde github:
Pasos para ejecutar:
1-Abrir Terminal cd ruta app. Ej: cd C:\Users\app
2-Una vez en el proyecto app, para activar el entorno virtual ejecutar: env/Scripts/activate 
3-Instalar django: pip install django si no lo tenemos instalado
4-Lanzar el proyecto: "python app/manage.py runserver"
5-Abrir navegador localhost:8000/users para visualizar la app de users que hemos creado para la prueba.
