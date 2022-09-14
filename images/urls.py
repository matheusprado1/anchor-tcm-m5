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
    ),  # Talitta-modifiquei essa url
    path(
        "image/<user_id>/", UserImageView.as_view()
    ),  # Talitta-adicionei essa url
    path("images/<image_id>/", ImageDetailView.as_view()),
]
