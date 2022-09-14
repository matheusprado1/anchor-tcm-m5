from django.urls import path

from .views import LoginView, UserDetailView, UserView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<uuid:user_id>/", UserDetailView.as_view()),
    path("login/", LoginView.as_view()),
]
