from django.urls import path

from .views import EventDetailView, EventDistanceView, ListCreateEventView

urlpatterns = [
    path("event/", ListCreateEventView.as_view()),
    path("event/<pk>/", EventDetailView.as_view()),
    path("event/distance/", EventDistanceView.as_view()),
]

