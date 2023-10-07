import time

from celery import Celery
from src.config import settings

app = Celery(settings.CELERY_APP_NAME,
             broker=settings.CELERY_BROKER_URL,
             backend=settings.CELERY_RESULT_BACKEND)


@app.task(name="create_task")
def create_task(message):
    time.sleep(5000)
    return f"return message : {message}"
