from django.urls import path

from .views import (
    EventDetailView,
    EventDistanceGteView,
    EventDistanceLteView,
    EventDistanceView,
    EventView,
)

urlpatterns = [
    path("event/", EventView.as_view()),
    path("event/id/<uuid:event_id>/", EventDetailView.as_view()),  # id
    path("event/distance/", EventDistanceView.as_view()),
    path("event/distance_lte/<int:dist>/", EventDistanceLteView.as_view()),
    path("event/distance_gte/<int:dist>/", EventDistanceGteView.as_view()),
]
