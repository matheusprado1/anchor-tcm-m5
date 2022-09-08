from django.urls import path
from .views import EventView

urlpatterns = [
  path("events/", EventView.as_view()),
  path("events/<event_id>/", EventView.as_view()),
]