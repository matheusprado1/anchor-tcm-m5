from django.urls import path

from .views import AddressesDetailView, AddressesView

urlpatterns = [
    path("addresses/", AddressesView.as_view()),
    path("addresses/<uuid:address_id>/", AddressesDetailView.as_view()),
]
