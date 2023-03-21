
from django.db import models

class Notification(models.Model):
    email = models.EmailField(max_length=30)
    is_autosend = models.BooleanField(default=False)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.email}"