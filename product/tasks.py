from csv import Error

from celery import shared_task
from time import sleep

@shared_task
def download():
    print("Запуск...")
    sleep(20)
    raise Error
    print("Успешно")
    return "OK"
