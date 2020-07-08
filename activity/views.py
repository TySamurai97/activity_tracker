from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from activity.serializers import UserSerializer, ActivityPeriodSerializer
from activity.models import User, ActivityPeriod


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
