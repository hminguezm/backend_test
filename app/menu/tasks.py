import logging
import os
from datetime import datetime

from celery.task.schedules import crontab
from celery.decorators import periodic_task

from app.menu.models import Menu
from app.services.slack import send_to_slack


@periodic_task(run_every=(crontab(minute='*/15')), name="send_menu", ignore_result=True)
def send_menu():
    date = datetime.utcnow()
    menu = Menu.objects.get(published_at=date)

    channel_menu = os.environ.get('SLACK_CHANNEL_SEND_TO_MENU')
    message_menu = 'nora.cornershop.io/menu/{}'.format(menu.id)

    try:
        response = send_to_slack(channel_menu, message_menu)
    except Exception as e:
        print("Error: %s" % e)
    else:
        logging.info(response.body)
