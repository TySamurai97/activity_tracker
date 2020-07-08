from rest_framework import serializers
from activity.models import ActivityPeriod, User

class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')

class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many = True)
    class Meta:
        model = User
        fields = ('user_id', 'real_name', 'tz', 'activity_periods')