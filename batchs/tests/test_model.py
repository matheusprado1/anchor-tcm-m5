import uuid

from django.test import TestCase
from model_bakery import baker


class BatchModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.zone = baker.make("zones.Zone")

    def test_one_to_many_relationship_is_made_zone(self):

        batch_1 = baker.make("batchs.Batch", zone=self.zone)

        self.assertEqual(batch_1.zone, self.zone)

    def test_uuid_pk(self):

        batch = baker.make("batchs.Batch")

        def is_valid_uuid(uuid_to_test, version=4):
            try:
                uuid_obj = uuid.UUID(str(uuid_to_test), version=version)
            except ValueError:
                return False
            return str(uuid_obj) == str(uuid_to_test)

        self.assertEqual(
            is_valid_uuid(batch.id),
            True,
            msg="Id is not uuid for batch",
        )