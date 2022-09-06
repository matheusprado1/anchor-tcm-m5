from django.urls import path

from . import views

urlpatterns = [
    path("addresses/", views.AddressesView.as_view()),
]
