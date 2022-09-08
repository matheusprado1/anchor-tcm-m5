from django.urls import path
from .views import ListCreateEventView, EventDetailView

urlpatterns = [
  path("events/", ListCreateEventView.as_view()),
  path("events/<event_id>/", EventDetailView.as_view()),
]