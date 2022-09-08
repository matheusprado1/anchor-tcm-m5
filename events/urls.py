from django.urls import path
from .views import EventView, EventDetailView

urlpatterns = [
  path("events/", EventView.as_view()),
  path("events/<event_id>/", EventDetailView.as_view()),
]