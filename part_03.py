from datetime import datetime
import os
import smtplib
import time
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465

'''tasks - словарь для задач'''
tasks = [
    {
        'title': 'complete homework',
        'time': datetime(2026, 10, 14, 19, 30),
        'completed': False
    },
    {
        'title': 'read a book',
        'time': datetime(2026, 10, 14, 20, 35),
        'completed': False
    },
    {
        'title': 'go to bed',
        'time': datetime(2026, 10, 14, 21, 30),
        'completed': False
    }
]

def send_email(task):
    '''функция отправки сообщения на почту с помощью smtp'''

    message = EmailMessage()

    message['From'] = EMAIL_ADDRESS
    message['To'] = EMAIL_ADDRESS
    message['Subject'] = 'напоминание о задаче'

    message.set_content(
        f'время выполнить задачу\n'
        f'задача : {task["title"]}\n'
        f'время : {task["time"]}\n'
    )

    server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.send_message(message)
    server.quit()

while True:

    now=datetime.now()
    for task in tasks:
        if not(task['completed']) and now >= task['time']:
            print()
            print('🔊🔊🔊 !!!напоминание!!! 🔊🔊🔊')
            send_email(task)

            task['completed'] = True
    time.sleep(3)