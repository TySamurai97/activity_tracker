from django.urls import path
from activity import views
from activity.views import UserView

urlpatterns = [
    path('users/', UserView.as_view()),
]