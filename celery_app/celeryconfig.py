from datetime import timedelta
from celery.schedules import crontab

broker_url = 'redis://127.0.0.1:6379'
result_backend = 'redis://127.0.0.1:6379/0'
timezone = 'Asia/Shanghai'

imports = (
    'celery_app.task1',
    'celery_app.task2'
)

beat_schedule = {
    'add-every-5-seconds':{
        'task': 'celery_app.task1.add',
        'schedule': timedelta(seconds=2),
        'args': (5, 8)
    },

    'multiply-at-some-time':{
        'task': 'celery_app.task2.multiply',
        'schedule': crontab(minute='*/1'),
        'args': (3, 7)
    }
}

