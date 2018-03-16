broker_url = 'redis://127.0.0.1:6379'
result_backend = 'redis://127.0.0.1:6379/0'
timezone = 'Asia/Shanghai'

imports = (
    'celery_app.task1',
     'celery_app.task2'
)
