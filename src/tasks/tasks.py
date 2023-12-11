import os
import time
import requests

from celery import Celery


celery = Celery('tasks', broker=os.getenv("CELERY_BROKER"))


@celery.task
def telegram(message: str) -> None:
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

