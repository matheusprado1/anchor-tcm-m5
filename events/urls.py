from django.urls import path

from .views import ListCreateEventView, EventDetailView, EventDistanceView


urlpatterns = [
  path("events/", ListCreateEventView.as_view()),
  path("events/<event_id>/", EventDetailView.as_view()),
  path("event/distance/", EventDistanceView.as_view()),
]

