from datetime import timedelta
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

celery_app = Celery('log_system')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')

celery_app.autodiscover_tasks()

celery_app.conf.broker_url = 'amqp://guest:guest@localhost:5672/' # for normal usage (without docker ) write your service name instead
celery_app.conf.result_backend = 'rpc://'
celery_app.conf.accept_content = ['json']
celery_app.conf.result_expires = timedelta(days=1)
celery_app.conf.worker_prefetch_multiplier = 1

@celery_app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')