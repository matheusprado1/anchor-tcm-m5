from uuid import UUID
from model_bakery import baker
from collections import OrderedDict

from rest_framework.views import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class TestTicketView(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:

        cls.commonUser = baker.make("users.User", is_superuser=False, birthdate="1900-01-01")
        cls.superUser = baker.make("users.User", is_superuser=True, birthdate="1900-01-01")
        cls.underageUser = baker.make("users.User", birthdate="2020-01-01")

        cls.commonUser_token = Token.objects.create(user=cls.commonUser).key
        cls.superUser_token = Token.objects.create(user=cls.superUser).key
        cls.underageUser_token = Token.objects.create(user=cls.underageUser).key
        cls.INVALID_token = "10351033"


        event = baker.make("events.Event", full_age=10)
        zone = baker.make("zones.Zone", event=event)

        batch_1 = baker.make("batchs.Batch", quantity=100, zone=zone, due_date="2100-01-01")
        batch_2 = baker.make("batchs.Batch", quantity=100, zone=zone, due_date="2100-01-01")
        old_batch = baker.make("batchs.Batch", quantity=100, zone=zone, due_date="2000-01-01")
        cls.small_batch = baker.make("batchs.Batch", quantity=1, zone=zone, due_date="2100-01-01")

        cls.ticket_data_1 = { "batch": str(batch_1.id) }
        cls.old_batch_ticket_data = { "batch": str(old_batch.id) }
        cls.small_batch_ticket_data = { "batch": str(cls.small_batch.id) }

        cls.UNEXISTING_batch_for_ticket_data = { "batch": "d3360bbe-e1c5-411f-9491-ddad5f700055" }
        cls.INVALID_type_for_ticket_data = { "batch": "10351033" }

        cls.ticket_list = baker.make("tickets.Ticket", _quantity=6, batch=batch_2)

        cls.path = "/api/tickets/"
    
    def test_create_ticket(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.commonUser_token}")
        response = self.client.post(self.path, self.ticket_data_1)

        expected_response = {
            "id": response.data["id"], 
            "user": self.commonUser.id, 
            "batch": UUID(self.ticket_data_1["batch"]), 
            "created_at": response.data["created_at"]
        }


        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expected_response)

    def test_create_muliple_tickets(self):

        for i in range(22):

            user = baker.make("users.User", birthdate="1900-01-01")
            user_token = Token.objects.create(user=user).key

            self.client.credentials(HTTP_AUTHORIZATION=f"Token {user_token}")
            response = self.client.post(self.path, self.ticket_data_1)

            expected_response = {
                "id": response.data["id"], 
                "user": user.id, 
                "batch": UUID(self.ticket_data_1["batch"]), 
                "created_at": response.data["created_at"]
            }

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(response.data, expected_response)


    def test_create_ticket_WITHOUT_token(self):

        response = self.client.post(self.path, self.ticket_data_1)

        expected_response = { "detail": "Authentication credentials were not provided." }

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, expected_response)

    def test_create_ticket_with_INVALID_token(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.INVALID_token}")
        response = self.client.post(self.path, self.ticket_data_1)

        expected_response = { "detail": "Invalid token." }

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, expected_response)

    def test_create_ticket_for_UNEXISTING_batch(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.commonUser_token}")
        response = self.client.post(self.path, self.UNEXISTING_batch_for_ticket_data)

        expected_response = {
            "batch": [
                f'Invalid pk \"{self.UNEXISTING_batch_for_ticket_data["batch"]}\" - object does not exist.'
        ]}

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)

    def test_create_ticket_with_EMPTY_body(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.commonUser_token}")
        response = self.client.post(self.path, {})

        expected_response = { "batch": ["This field is required."] }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)

    def test_create_ticket_with_INVALID_batchId_type(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.commonUser_token}")
        response = self.client.post(self.path, self.INVALID_type_for_ticket_data)

        expected_response = {
            "batch": [f'“{self.INVALID_type_for_ticket_data["batch"]}” is not a valid UUID.']
        }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)

    def test_create_ticket_with_INSUFICIENT_age_for_user(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.underageUser_token}")
        response = self.client.post(self.path, self.ticket_data_1)

        expected_response = {"detail": "Not old enought to buy ticket"}

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, expected_response)

    def test_create_ticket_from_OVERDUE_batch(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.commonUser_token}")
        response = self.client.post(self.path, self.old_batch_ticket_data)

        expected_response = {"detail": "Batch over due date"}

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, expected_response)

    def test_create_ticket_with_INSUFICIENT_ticket_quantity(self):

        baker.make("tickets.Ticket", batch=self.small_batch)

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.commonUser_token}")
        response = self.client.post(self.path, self.small_batch_ticket_data)

        expected_response = {"detail": "Not enought tickets on this batch"}

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, expected_response)

    def test_list_tickets(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.superUser_token}")
        response = self.client.get(self.path)

        results = [
            OrderedDict([ 
                ("id", str(self.ticket_list[i].id)),
                ("user", self.ticket_list[i].user_id),
                ("batch", self.ticket_list[i].batch_id),
                ("created_at", self.ticket_list[i].created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
        ]) for i in range(4)]
        
        expected_response = OrderedDict([
            ("count", len(self.ticket_list)), 
            ("next", f"http://testserver{self.path}?page=2"), 
            ("previous", None), 
            ("results", results)
        ])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_paginate_in_list_tickets(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.superUser_token}")
        response = self.client.get(f"{self.path}?page=2")

        results = [
            OrderedDict([ 
                ("id", str(self.ticket_list[i].id)),
                ("user", self.ticket_list[i].user_id),
                ("batch", self.ticket_list[i].batch_id),
                ("created_at", self.ticket_list[i].created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
        ]) for i in range(4,6)]
        
        expected_response = OrderedDict([
            ("count", len(self.ticket_list)), 
            ("next", None), 
            ("previous", f"http://testserver{self.path}"), 
            ("results", results)
        ])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)
    
    def test_list_tickets_with_INVALID_permission(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.commonUser_token}")
        response = self.client.get(self.path)

        expected_response = { "detail": "You do not have permission to perform this action." }

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, expected_response)

