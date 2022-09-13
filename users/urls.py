from django.urls import path

from .views import ImageView, LoginView, UserDetailView, UserView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/images/<str:user_id>/", ImageView.as_view()),
    path("users/<str:user_id>/", UserDetailView.as_view()),
    path("login/", LoginView.as_view()),
]
