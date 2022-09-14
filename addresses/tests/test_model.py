import uuid

from addresses.models import Address
from django.test import TestCase
from events.models import Event
from model_bakery import baker


class AddressModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.address_1 = baker.make("Address")
        cls.address_2 = baker.make("Address")
        cls.user_1 = baker.make("users.User", address=cls.address_1)
        cls.event_1 = Event.objects.create(
            name="evento1",
            description="Vai ser um evento muito divertido",
            duration=555,
            date="1999-09-08 13:56:51.715538+00",
            classification=16,
            address=cls.address_2,
        )

    def test_one_to_one_relationship_is_made_user(self):
        print("executando test_one_to_one_relationship_is_made_user")

        self.assertEqual(self.user_1.address, self.address_1)

    def test_one_to_one_relationship_is_made_event(self):
        print("executando test_one_to_one_relationship_is_made_event")

        self.assertEqual(self.event_1.address, self.address_2)

    def test_uuid_pk(self):
        print("executando test_uuid_pk_address")

        def is_valid_uuid(uuid_to_test, version=4):
            try:
                uuid_obj = uuid.UUID(str(uuid_to_test), version=version)
            except ValueError:
                return False
            return str(uuid_obj) == str(uuid_to_test)

        self.assertEqual(
            is_valid_uuid(self.address_1.id),
            True,
            msg="Id is not uuid for product",
        )

    def test_address_fields_constraints(self):
        print("executando test_address_fields_constraints")

        max_length_city = Address._meta.get_field("city").max_length
        self.assertEqual(max_length_city, 50)

        max_length_district = Address._meta.get_field("district").max_length
        self.assertEqual(max_length_district, 100)

        max_length_street = Address._meta.get_field("street").max_length
        self.assertEqual(max_length_street, 255)

        max_length_number = Address._meta.get_field("number").max_length
        self.assertEqual(max_length_number, 30)

        max_length_zipcode = Address._meta.get_field("zipcode").max_length
        self.assertEqual(max_length_zipcode, 20)
