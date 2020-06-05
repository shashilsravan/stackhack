from celery import shared_task
from time import sleep
from django.core.mail import send_mail

@shared_task
def send_email_task(title, content, recipient):
    send_mail(title, content,
              'sravanshashil@gmail.com', [recipient])
    return None