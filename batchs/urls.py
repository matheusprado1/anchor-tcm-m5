from django.urls import path

from .views import BatchsView, UpdateBatchsView

urlpatterns = [
    path("batchs/", BatchsView.as_view()),
    path("batchs/<uuid:batch_id>/", UpdateBatchsView.as_view()),
]
