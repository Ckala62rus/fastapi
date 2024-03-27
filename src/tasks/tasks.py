import os
import time
import requests

from celery import Celery


celery = Celery('tasks', broker=os.getenv("CELERY_BROKER"))
# celery.config_from_object(Config)


@celery.on_after_configure.connect
def setup_periodic_tasks(sender: Celery, **kwargs):
    sender.add_periodic_task(20.0, check)


@celery.task
def check():
    url = "https://api.telegram.org/bot6823753558:AAEOS7wEBxIMUnBbRBK-t4PqRxA8hfvAIYs/sendMessage"
    response = requests.get(
        url,
        params={
            "chat_id": 803431360,
            "text": "test test test"
        }
    )


@celery.task
def telegram(message: str) -> None:
    print("Hello!")
    time.sleep(5)
    token = os.getenv("TELEGRAM_BOT_TOKEN", "(example)5853484688:AAFzfJEjnHv3AMgWCpO5bsj6UhqgusvnkZc")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.get(
        url,
        params={
            # example (int) chat id
            "chat_id": 803431360,
            "text": message
        }
    )

