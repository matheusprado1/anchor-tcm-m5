from django.urls import path

from .views import BatchsView, UpdateBatchsView

urlpatterns = [
    path("batch/", BatchsView.as_view()),
    path("batch/<uuid:pk>/", UpdateBatchsView.as_view()),
]
