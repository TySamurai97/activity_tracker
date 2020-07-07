from django.shortcuts import render
from activity.models import User, ActivityPeriod

# Create your views here.
def users_index(request):
    