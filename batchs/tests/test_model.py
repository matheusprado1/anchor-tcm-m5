from django.test import TestCase
from model_bakery import baker
import uuid


class BatchModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.batch_1 = baker.make("Batch")
        cls.batch_2 = baker.make("Batch")
        cls.event = baker.make("events.Event", id=cls.batch_1.id)

    def test_one_to_many_relationship_is_made_event(self):

       self.assertEqual(self.event.batch_1, self.batch_1)

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
            msg="Id is not uuid for batch"
        )
