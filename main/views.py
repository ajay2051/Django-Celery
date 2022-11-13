from django.shortcuts import render
from django.http import HttpResponse
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

from .tasks import test_func
from mail.tasks import send_mail_func

# Create your views here.

def home(request):
    test_func.delay()
    return HttpResponse("Hello")


def send_mail(request):
    send_mail_func.delay()
    return HttpResponse('Mail Sent Success')


#Send Tasks Dynamically
def send_mail_at_particular_time(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=0, minutes=0)
    task = PeriodicTask.objects.create(crontab=schedule, name='schedule_mail_task' + '1', task = 'mail.tasks.send_mail_func', args=json.dumps([[2,3]]))
    return HttpResponse('Mail Sent at Particular Time')
