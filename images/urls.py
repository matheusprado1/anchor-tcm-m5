from django.urls import path

from .views import (
    EventImageView,
    EventListImageView,
    UserImageView,
    UserImageDetailView,
)

urlpatterns = [
    path("images/", EventListImageView.as_view()),
    path(
        "image/<event_id>/", EventImageView.as_view()
    ),
    path(
        "image/<user_id>/", UserImageView.as_view()
    ),
    path("images/<image_id>/", UserImageDetailView.as_view()),
]

