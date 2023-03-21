from time import sleep

from celery import shared_task
from django.core.mail import send_mail
from django.core.management import call_command

from .models import Notification

@shared_task()
def send_feedback_notification_task(notification_id):
    """Sends an email when the feedback form has been submitted."""
    print("Run Offloading task")
    sleep(5)
    try:
        notification = Notification.objects.get(id=notification_id)
        email_address = notification.email
        message = notification.description

        send_mail(
            "Your Feedback",
            f"\t{message}\n\nThank you!",
            "support@example.com",
            [email_address],
            fail_silently=False,
        )
    except:
        print(f"Cant get notification of notification_id: {notification_id}")


@shared_task
def send_notification_every_min():
    call_command("notification_every_min", )

