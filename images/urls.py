from django.urls import path

from .views import ImageDetailView, ImageView, ListImageView

urlpatterns = [
    path("images/", ListImageView.as_view()),
    path("image/<event_id>/", ImageView.as_view()),
    path("images/<image_id>/", ImageDetailView.as_view())
]

