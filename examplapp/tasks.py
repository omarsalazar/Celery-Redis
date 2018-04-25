from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task, periodic_task
from CeleryExample.celery import app
from django.core.mail import EmailMessage


@task(name="sum_two_numbers")
def add(x, y):
    return x + y


@task(name="multiply_two_numbers")
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    return total


@task(name="rest")
def area(x, y):
    total = x - y
    return total


@app.task
def email(data):
    asunto = 'Test de Celery con Redis'
    mensaje = 'Hola Robert, esto es un mensaje de prueba'
    mail = EmailMessage(asunto, mensaje, to=[data])
    try:
        mail.send()
    except Exception as e:
        print(e)
        print(type(e))
    return data


@app.task
def funcioni(x, func, *args):
    func(*args)
    for i in range(1, x):
        print("Holongo")
