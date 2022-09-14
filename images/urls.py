from django.urls import path
from .views import (
    EventImageView,
    ImageDetailView,
    ListImageView,
    UserImageView,
)

urlpatterns = [
    path("images/", ListImageView.as_view()),
    path(
        "image/<event_id>/", EventImageView.as_view()
    ),
    path(
        "image/<user_id>/", UserImageView.as_view()
    ),
    path("images/<image_id>/", ImageDetailView.as_view()),
]