from django.urls import path

from tickets.views import TicketDeleteView, TicketView, TicketRetrieveView

urlpatterns = [
    path("ticket/", TicketView.as_view()),
    path("ticket/<user_id>/", TicketRetrieveView.as_view()),
    path("tickets/<ticket_id/", TicketDeleteView.as_view())
]