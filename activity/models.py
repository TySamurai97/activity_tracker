from django.db import models
import uuid

class User(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=50)

class ActivityPeriod(models.Model):
    activity_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activity_periods')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()