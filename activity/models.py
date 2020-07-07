from django.db import models


# Create your models here.
class User(models.Model):
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=50)

class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()