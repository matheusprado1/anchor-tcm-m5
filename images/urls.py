from django.urls import path

from .views import (
    EventImageView,
    EventListImageView,
    UserImageView,
    ImageDetailView,

)

urlpatterns = [
    path("images/", EventListImageView.as_view()),
    path(
        "images/events/<event_id>/", EventImageView.as_view()
    ),
    path(
        "images/users/<user_id>/", UserImageView.as_view()
    ),
    path("images/view/<image_id>/", ImageDetailView.as_view()),
]
