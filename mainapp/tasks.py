from email import message_from_string
from django.core.mail import send_mail
from celery import shared_task

from django.contrib.auth import get_user_model

@shared_task
def send_feedback_to_email(message_from, body):
    model_user = get_user_model()
    if not model_user:
        model_user = "Аноним"

    send_mail(f'Feedback from {message_from}', #subject
    message=body,
    recipient_list=['gas53@bk.ru'],
    from_email='gas53@bk.ru',
    fail_silently=False)