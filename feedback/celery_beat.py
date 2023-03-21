from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json
from datetime import datetime, timedelta


schedule, created = IntervalSchedule.objects.get_or_create(
    every=30,
    period=IntervalSchedule.SECONDS,
)


PeriodicTask.objects.create(
    interval=schedule,                  # we created this above.
    name='Send Notifications',          # simply describes this periodic task.
    task='.tasks.send_feedback_notification_task',  # name of task.
    # args=json.dumps(['arg1', 'arg2']),
    kwargs=json.dumps({
       'notification_id': 1,
    }),
    # expires=datetime.utcnow() + timedelta(seconds=30)
)
