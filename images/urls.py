from django.urls import path

from .views import ImageDetailView, ImageView, ListImageView

urlpatterns = [
    path("images/", EventListImageView.as_view()),
    path("image/<event_id>/", EventImageView.as_view()),
    path("images/<image_id>/", EventImageDetailView.as_view())
]

