from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('send-mail/',views.send_mail, name='send_mail'),
    path('schedule-mail/',views.send_mail_at_particular_time, name='schedule_mail'),
]