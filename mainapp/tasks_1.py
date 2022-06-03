from django.core import mail


def send_feedback_mail(*args):
    connection = mail.get_connection()
    with connection as conn:
        email1 = mail.EmailMessage(
            'Hello',
            'Body goes here',
            'gas53@bk.ru',
            ['gas53@bk.ru'],
            connection=conn,
        )
        email1.send()

send_feedback_mail()