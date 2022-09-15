#actors/tests/test_models.py
from django.test import TestCase
from events.models import Event

class EventModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.name = "Festa do pijama"
        cls.description = "Festa super legal"
        cls.duration = 4
        cls.date = "2022-10-10"
        cls.classification = 18

        cls.event = Event.objects.create(
            name=cls.name,
            description=cls.description,
            duration=cls.duration,
            date=cls.date,
            classification=cls.classification
        )

    def test_name_max_length(self):
        event = Event.objects.get(id=self.event.id)
        max_length = event._meta.get_field('name').max_length
        self.assertEquals(max_length, 127)

    def test_event_has_information_fields(self):
        self.assertEqual(self.event.name, self.name)
        self.assertEqual(self.event.description, self.description)
        self.assertEqual(self.event.duration, self.duration)
        self.assertEqual(self.event.date, self.date)
        self.assertEqual(self.event.classification, self.classification)