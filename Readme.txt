He creado un proyecto Python con el Framework Django, para ello he creado un entorno virtual,necesario para dicho framework,
en la carpeta env con "pip install virtualenv" y "python -m venv env" para darle el nombre env a dicho entorno.

Dentro del proyecto app tenemos la app principal que enlaza con la aplicación users, que es la aplicación que se ha realizado para
la prueba.
Para este proyecto he usado phpmyadmin para crear una  base de datos. Adjunto el fichero de bbdd exportado listo para 
importar llamado connections.sql(viene incluido en el proyecto de github)
Para los estilos he instalado e integrado bootstrap.

descargar desde github: https://github.com/danielvega3009/DaniVegaPrueba.git
Pasos para ejecutar:
1-Abrir Terminal cd ruta app. Ej: "cd C:\Users\app"
2-Una vez en el proyecto app, para activar el entorno virtual ejecutar: env/Scripts/activate 
3-Instalar django: "pip install django" si no lo tenemos instalado
4-Instalar bootstrap para los estilos: pip install django-bootstrap4
5-Iniciar servidor Apache.
6-Importar en la bbdd el fichero connections.sql
7-Lanzar el proyecto: "python app/manage.py runserver"
8-Abrir navegador localhost:8000/users para visualizar la app de users que hemos creado para la prueba.

Acciones disponibles en la aplicación:
  Crear  Usuario con usuario conectado
  Editar la conexión de dichos usuarios
  Eliminar la conexión de dichos usuarios
  Ver detalles del usuario y su conectado
  Ver los usuarios conectados con el usuario de la fila seleccionada
