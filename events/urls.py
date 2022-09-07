from django.urls import path
from .views import EventDetailView, EventView

urlpatterns = [
  path("event/", EventView.as_view()),
  path("event/<event_id>/", EventDetailView.as_view()),
]