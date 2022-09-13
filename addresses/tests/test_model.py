import uuid

from django.test import TestCase
from model_bakery import baker


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.address_1 = baker.make("Address")
        cls.address_2 = baker.make("Address")
        cls.user_1 = baker.make("users.User", address=cls.address_1)
        # cls.event_1 = baker.make("Event", address=cls.address_2)

    def test_one_to_one_relationship_is_made(self):
        ...
        # print("executando test_one_to_one_relationship_is_made")

        # self.assertEqual(self.user_1.address, self.address_1)
