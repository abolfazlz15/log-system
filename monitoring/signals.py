from django.db.models.signals import post_save
from django.dispatch import receiver

from monitoring.models import LogEntry
from monitoring.tasks import send_error_email


@receiver(post_save, sender=LogEntry)
def  notification_handler_signal(sender, instance, created, *args, **kwargs):
    if created:
        data = f'{instance.date_time} {instance.user} {instance.method} {instance.status}'
        if instance.status > 300:
            send_error_email.delay(data)