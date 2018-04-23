# Celery-Redis
Making an example of Celery with Redis

### Guía de instalación.

#### Clona el proyecto.
```
git clone https://github.com/omarsalazar/Celery-Redis
cd Celery-Redis
```

#### Entorno virtual

Instalación del entorno.
```
pip install python-virtualenv
```
Creación del entorno virtual.
```
virtualenv -p python3 myvenv
```
Activación.
```
source myvenv/bin/activate
```

#### Instalación de dependencias.
```
pip install -r requirements.txt
```
### Ejecuta el proyecto.
```
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
´´´
En otra terminal.
´´´
Celery -A cfehome worker -l info
´´´
En otra terminal.
´´´
celery -A cfehome beat -l info
´´´
