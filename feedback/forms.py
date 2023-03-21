from django import forms
from feedback.tasks import send_feedback_notification_task
from django.core.cache import cache
from .models import Notification

class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={"rows": 5})
    )
    is_autosend = forms.BooleanField(label="Auto", required=False, initial=False)

    def send_notification(self):
        if cache.get(self.cleaned_data["email"]): return

        notification = Notification(
            email = self.cleaned_data["email"],
            description = self.cleaned_data["message"],
            is_autosend = self.cleaned_data["is_autosend"]
        )
        notification.save()

        send_feedback_notification_task.delay(
            notification.id
        )
        cache.set(self.cleaned_data["email"], 'message', 30)
