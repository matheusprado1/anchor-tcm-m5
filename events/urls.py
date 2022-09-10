from django.urls import path

from .views import ListCreateEventView, EventDetailView


urlpatterns = [
  path("events/", ListCreateEventView.as_view()),
  path("events/<pk>/", EventDetailView.as_view()),
    path("event/distance/", EventDistanceView.as_view()),
]

