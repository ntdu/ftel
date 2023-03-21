from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail
from feedback.models import Notification

class Command(BaseCommand):
    help = "A description of the command"

    def add_arguments(self, parser):
        parser.add_argument('notification_id', nargs='?', type=str)

    def handle(self, *args, **options):
        for notification in Notification.objects.filter(is_autosend=True):
            email_address = notification.email
            message = notification.description

            send_mail(
                "Your Feedback",
                f"\t{message}\n\nThank you!",
                "support@example.com",
                [email_address],
                fail_silently=False,
            )