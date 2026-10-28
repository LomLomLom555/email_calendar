from datetime import datetime
import os
import smtplib
import time
from email.message import EmailMessage
import json

from dotenv import load_dotenv

load_dotenv()
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465

TASKS_FILE = 'tasks.json'

def load_tasks():
    '''загружаем задачу из файла'''
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    '''функция сохранения задач'''
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, ensure_ascii = False, indent=4)

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

def add_task(tasks):
    '''добавляем задачу'''
    title = input('название задачи: ')
    date = input('дата (ГГГГ-ММ-ДД): ')
    task_time = input('время (ЧЧ-ММ): ')
    try:
        datetime.strptime(
            f'{date},{task_time}', '%Y-%m-%d %H:%M:%S'
        )
    except ValueError:
        return

    task = {
        'title': title,
        'time': f'{date} {task_time}',
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)

    print('задача добавлена (ура)')
