from rest_framework import generics
from rest_framework.views import Response, status

from batchs.erros import (
    AgeValidationError,
    DataValidationError,
    TicketValidationError,
)

from batchs.models import Batch
from tickets.models import Ticket
from tickets.serializers import TicketSerializer

from tickets.permissions import (
    IsSuperuser,
    IsSuperuserOrAuthenticatedToCreate,
    IsSuperuserOrIsOwner,
    IsUser,
)


class TicketView(generics.ListCreateAPIView):
    permission_classes = [IsSuperuserOrAuthenticatedToCreate]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        batch = Batch.objects.get( pk=serializer.validated_data["batch"].id )
        user = self.request.user

        try:
            if user.age() < batch.zone.event.classification:
                raise AgeValidationError
            if batch.is_date_valid() is False:
                raise DataValidationError
            if batch.is_enough_tickets() is False:
                raise TicketValidationError

        except AgeValidationError:
            return Response(
                {"detail": "Not old enought to buy ticket"},
                status.HTTP_403_FORBIDDEN,
            )
        except DataValidationError:
            return Response(
                {"detail": "Batch over due date"}, status.HTTP_403_FORBIDDEN
            )
        except TicketValidationError:
            return Response(
                {"detail": "Not enought tickets on this batch"},
                status.HTTP_403_FORBIDDEN,
            )

        serializer.save(batch=batch, user=user)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class UserTicketsView(generics.ListAPIView):
    permission_classes = [IsSuperuser | IsUser]

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_queryset(self):
        return self.queryset.filter(user_id=self.kwargs["user_id"])


class TicketDeleteView(generics.DestroyAPIView):

    lookup_url_kwarg = "ticket_id"
    permission_classes = [IsSuperuserOrIsOwner]

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer