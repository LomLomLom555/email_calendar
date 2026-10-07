from datetime import datetime
import os
import smtplib
import time
import json

task = 'убраться в комнате'

task_time = datetime(2026,10,7,19,53)

now = datetime.now()
print('=*='*50)
print('моя задача')
print('=*='*50)
print(f'задача: {task.capitalize()}')
print(f'выполнить: {task_time}')
print('=*='*50)
print()
print(f'текущее время: {now}')

if now >= task_time:
    print()
    print('✔✔✔время выполнять задачу✔✔✔')

else:
    print()
    print('🎈🎈🎈ещё не выполнять задачу📣📣📣')