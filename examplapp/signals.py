from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
from .tasks import email
from .models import UserData
from datetime import datetime, timedelta
send_date = datetime.utcnow() + timedelta(seconds=1)

@receiver(post_save, sender=UserData)
def create_user(sender, instance, created, **kwards):
    try:
        import pudb; pudb.set_trace()
        if created:
            print('holis')
            email.apply_async((1,), eta=send_date)
    except Exception as e:
        print('error')
        print(e)
