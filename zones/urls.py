from django.urls import path

from .views import ZoneDetailView, ZoneView

urlpatterns = [
  path("zones/", ZoneView.as_view()),
  path("zones/<int:zone_id>/", ZoneDetailView.as_view()),
]
