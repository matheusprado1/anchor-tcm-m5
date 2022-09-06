from django.urls import path

from . import views

urlpatterns = [
    path("batch/", views.BatchsView.as_view()),
    path("batch/<uuid:pk>/", views.UpdateBatchsView.as_view()),
]
