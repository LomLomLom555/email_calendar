from datetime import datetime
import time

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

while True:

    now=datetime.now()
    for task in tasks:
        if not(task['completed']) and now >= task['time']:
            print()
            print('🔊🔊🔊 !!!напоминание!!! 🔊🔊🔊')
            print(f'задача:{task["title"]}')
            print(f'time:{task["time"]}')
            task['completed'] = True
    time.sleep(3)
