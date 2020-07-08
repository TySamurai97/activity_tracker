from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from activity.serializers import UserSerializer, ActivityPeriodSerializer
from activity.models import User, ActivityPeriod
from pytz import all_timezones, timezone
from datetime import datetime
from django.utils.timezone import make_aware

class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def populate_dummy_data(request):
    mic = User(real_name = 'Michael Scott', tz = all_timezones[168])
    mic.save()
    jim = User(real_name = 'Jim Halpert', tz = all_timezones[169])
    jim.save()
    pam = User(real_name = 'Pam Beesly', tz = all_timezones[170])
    pam.save()
    ap1 = ActivityPeriod(user = mic, start_time = make_aware(datetime(2020 ,4 ,25 ,9 ,30 , 0), timezone = timezone(mic.tz)), end_time = make_aware(datetime(2020 ,4 ,25 ,17 ,30 , 0), timezone = timezone(mic.tz)))
    ap1.save()
    ap2 = ActivityPeriod(user = mic, start_time = make_aware(datetime(2020 ,6 ,25 ,9 ,30 , 0), timezone = timezone(mic.tz)), end_time = make_aware(datetime(2020 ,6 ,25 ,13 ,30 , 0), timezone = timezone(mic.tz)))
    ap2.save()
    ap3 = ActivityPeriod(user = mic, start_time = make_aware(datetime(2020 ,1 ,1 ,9 ,30 , 0), timezone = timezone(mic.tz)), end_time = make_aware(datetime(2020 ,1 ,2 ,17 ,30 , 0), timezone = timezone(mic.tz)))
    ap3.save()
    ap4 = ActivityPeriod(user = jim, start_time = make_aware(datetime(2020 ,6 ,25 ,9 ,30 , 0), timezone = timezone(jim.tz)), end_time = make_aware(datetime(2020 ,6 ,25 ,13 ,30 , 0), timezone = timezone(jim.tz)))
    ap4.save()
    ap5 = ActivityPeriod(user = jim, start_time = make_aware(datetime(2020 ,1 ,1 ,9 ,30 , 0), timezone = timezone(jim.tz)), end_time = make_aware(datetime(2020 ,1 ,2 ,17 ,30 , 0), timezone = timezone(jim.tz)))
    ap5.save()
    ap6 = ActivityPeriod(user = pam, start_time = make_aware(datetime(2020 ,1 ,1 ,9 ,30 , 0), timezone = timezone(pam.tz)), end_time = make_aware(datetime(2020 ,1 ,2 ,17 ,30 , 0), timezone = timezone(pam.tz)))
    ap6.save()
    return Response({'dummy_insert': 'Success'}, status = status.HTTP_200_OK)