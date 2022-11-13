from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from celery_project import settings
from django.utils import timezone

@shared_task(bind=True)
def send_mail_func(self, a, b):
    users = get_user_model().objects.all()
    timezone.localtime(users.datetimes)
    for user in users:
        mail_subject = 'Hi Celery Mail'
        message = 'This is tesitng celery mail'
        to_email = user.email
        send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True,
        )
    return ("Mail Send")
        