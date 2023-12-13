from celery import shared_task
from django.core.mail import send_mail
from core.settings import EMAIL_HOST_USER, EMAIL_SUPPORT

@shared_task
def send_error_email(log_data):
    '''celery task to send ERROR log level email'''
    subject = 'Error Notification'
    message = f'An error occurred:\n\n{log_data}'
    from_email = EMAIL_HOST_USER
    to_email = EMAIL_SUPPORT 

    send_mail(subject, message, from_email, [to_email])
