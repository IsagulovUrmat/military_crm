from django.core.mail import EmailMessage
from django.contrib.auth.models import User, Group

def mailing(username):

    users = User.objects.filter(is_superuser=True)

    email_list = []
    for user in users:
        email_list.append(user.email)


    subject = 'Greetings'
    body = f'User with {username} registered in military database, pls check him!'

    email = EmailMessage(subject=subject, body=body, to=email_list)
    email.send()



