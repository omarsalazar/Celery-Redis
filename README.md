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

#### [Redis](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-redis-on-ubuntu-16-04)

```
sudo systemctl start redis
sudo systemctl status redis

```

#### Celery

En otra terminal.
```
celery -A CeleryExample worker -l info
```
En otra terminal.
```
celery -A CeleryExample beat -l info
```
