from django.urls import path

from . import views

urlpatterns = [
  path("zones/", views.ZoneView.as_view()),
]