import uuid

from django.test import TestCase
from events.models import Event
from model_bakery import baker
from zones.models import Zone


class ZoneModelTest(TestCase):
  @classmethod
  def setUpTestData(cls) -> None:
    cls.event = baker.make("events.Event")

  def test_one_to_many_relationship_is_made_event(self):
    zone_1 = baker.make("zones.Zone", event=self.event)
    zone_2 = baker.make("zones.Zone", event=self.event)

    self.assertEqual(zone_1.event, self.event)
    self.assertEqual(zone_2.event, self.event)


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
