from django.urls import path

from .views import EventDetailView, EventDistanceView, EventView

urlpatterns = [
    path("event/", EventView.as_view()),
    path("event/<pk>/", EventDetailView.as_view()),
    path("event/distance/", EventDistanceView.as_view()),
]

