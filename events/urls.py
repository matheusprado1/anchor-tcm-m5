from django.urls import path

from .views import (
    EventDetailView,
    EventDistanceGteView,
    EventDistanceLteView,
    EventDistanceView,
    ListCreateEventView,
)

urlpatterns = [
    path("events/", ListCreateEventView.as_view()),
    path("events/<uuid:event_id>/", EventDetailView.as_view()),
    path("event/distance/", EventDistanceView.as_view()),
    path("event/distance_lte/<int:dist>/", EventDistanceLteView.as_view()),
    path("event/distance_gte/<int:dist>/", EventDistanceGteView.as_view()),
]
