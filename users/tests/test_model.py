import uuid
from django.test import TestCase
from model_bakery import baker


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.address = baker.make("addresses.Address")

    def test_one_to_many_relationship_is_made_address(self):

        user_1 = baker.make("users.Users", address=self.address)
        user_2 = baker.make("users.Users", address=self.address)

        self.assertEqual(user_1.address, self.address)
        self.assertEqual(user_2.address, self.address)

    def test_uuid_pk(self):

        user = baker.make("users.User")

        def is_valid_uuid(uuid_to_test, version=4):
            try:
                uuid_obj = uuid.UUID(str(uuid_to_test), version=version)
            except ValueError:
                return False
            return str(uuid_obj) == str(uuid_to_test)

        self.assertEqual(
            is_valid_uuid(user.id),
            True,
            msg="Id is not uuid for user",
        )
