from django.core.mail import send_mail

import environ

env = environ.Env()
environ.Env.read_env()

#
def my_send_email(data):
    send_mail(
        data['subject'],
        data['message'],
        env('GMAIL_USERNAME'),
        data['to'],
        fail_silently=False,
        )
