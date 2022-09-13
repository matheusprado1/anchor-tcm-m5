import uuid
from django.test import TestCase
from model_bakery import baker


class TicketModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.user = baker.make("users.User")
        cls.batch = baker.make("batchs.Batch", quantity=100)

    def test_one_to_many_relationship_is_made_user(self):

        ticket_1 = baker.make("tickets.Ticket", user=self.user)
        ticket_2 = baker.make("tickets.Ticket", user=self.user)

        self.assertEqual(ticket_1.user, self.user)
        self.assertEqual(ticket_2.user, self.user)

    def test_one_to_many_relationship_is_made_batch(self):

        ticket_1 = baker.make("tickets.Ticket", batch=self.batch)
        ticket_2 = baker.make("tickets.Ticket", batch=self.batch)

        self.assertEqual(ticket_1.batch, self.batch)
        self.assertEqual(ticket_2.batch, self.batch)

    def test_uuid_pk(self):

        ticket = baker.make("tickets.Ticket")

        def is_valid_uuid(uuid_to_test, version=4):
            try:
                uuid_obj = uuid.UUID(str(uuid_to_test), version=version)
            except ValueError:
                return False
            return str(uuid_obj) == str(uuid_to_test)

        self.assertEqual(
            is_valid_uuid(ticket.id),
            True,
            msg="Id is not uuid for product",
        )
