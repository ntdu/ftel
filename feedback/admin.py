# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Notification

# Register your models here.

class NotificationAdmin(admin.ModelAdmin):
  list_display = ("email", "is_autosend", "description",)
  
admin.site.register(Notification, NotificationAdmin)