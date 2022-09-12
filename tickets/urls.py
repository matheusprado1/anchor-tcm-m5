from django.urls import path

from tickets.views import TicketView, UserTicketsView, TicketDeleteView

urlpatterns = [
    path("tickets/", TicketView.as_view()),
    path("tickets/user/<user_id>/", UserTicketsView.as_view()),
    path("tickets/<ticket_id>/", TicketDeleteView.as_view())
]