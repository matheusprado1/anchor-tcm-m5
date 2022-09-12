from model_bakery import baker
from collections import OrderedDict

from rest_framework.views import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class TestTicketView(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:

        cls.commonUser = baker.make("users.User")
        cls.superUser = baker.make("users.User", is_superuser=True)

        cls.commonUser_token = Token.objects.create(user=cls.commonUser).key
        cls.superUser_token = Token.objects.create(user=cls.superUser).key
        cls.INVALID_token = "10351033"

        cls.batch_1 = baker.make("batchs.Batch", quantity=100)
        cls.batch_2 = baker.make("batchs.Batch", quantity=100)

        cls.ticket_data_1 = { "batch_id": str(cls.batch_1.batch_id) }

        cls.INVALID_ticket_data = { "batch_id": "d3360bbe-e1c5-411f-9491-ddad5f700055" }
        cls.INVALID_type_for_ticket_data = { "batch_id": "1" }

        cls.ticket_list = [baker.make("tickets.Ticket", batch_id=cls.batch_2.batch_id) for i in range(6)]

        cls.path = "/api/tickets/"
    
    def test_create_ticket(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.commonUser_token}")
        response = self.client.post(self.path, self.ticket_data_1)

        expected_response = {
            "id": response.data["id"], 
            "user_id": self.commonUser.id, 
            "batch_id": self.ticket_data_1["batch_id"], 
            "created_at": response.data["created_at"]
        }

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expected_response)

    def test_create_muliple_tickets(self):

        for i in range(22):

            user = baker.make("users.User")
            user_token = Token.objects.create(user=user).key

            self.client.credentials(HTTP_AUTHORIZATION=f"Token {user_token}")
            response = self.client.post(self.path, self.ticket_data_1)

            expected_response = {
                "id": response.data["id"], 
                "user_id": user.id, 
                "batch_id": self.ticket_data_1["batch_id"], 
                "created_at": response.data["created_at"]
            }

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(response.data, expected_response)


    def test_create_ticket_WITHOUT_token(self):

        response = self.client.post(self.path, self.ticket_data_1)

        expected_response = {
            "detail": "Authentication credentials were not provided."
        }

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, expected_response)

    def test_create_ticket_with_INVALID_token(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.INVALID_token}")
        response = self.client.post(self.path, self.ticket_data_1)

        expected_response = {
            "detail": "Invalid token."
        }

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, expected_response)

    def test_create_ticket_for_UNEXISTING_batch(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.commonUser_token}")
        response = self.client.post(self.path, self.INVALID_ticket_data)

        expected_response = { "detail": "Not found." }

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, expected_response)

    def test_create_ticket_with_EMPTY_body(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.commonUser_token}")
        response = self.client.post(self.path, {})

        expected_response = { "batch_id": ["This field is required."] }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)

    def test_create_ticket_with_INVALID_batchId_type(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.commonUser_token}")
        response = self.client.post(self.path, self.INVALID_type_for_ticket_data)

        expected_response = { "batch_id": ["Must be a valid UUID."] }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)


    def test_list_tickets(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.superUser_token}")
        response = self.client.get(self.path)

        results = [
            OrderedDict([ 
                ("id", str(self.ticket_list[i].id)),
                ("user_id", self.ticket_list[i].user_id),
                ("batch_id", str(self.ticket_list[i].batch_id)),
                ("created_at", self.ticket_list[i].created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
        ]) for i in range(4)]
        
        expected_response = OrderedDict([
            ("count", len(self.ticket_list)), 
            ("next", "http://testserver/api/tickets/?page=2"), 
            ("previous", None), 
            ("results", results)
            ])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_paginate_in_list_tickets(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.superUser_token}")
        response = self.client.get("/api/tickets/?page=2")

        results = [
            OrderedDict([ 
                ("id", str(self.ticket_list[i].id)),
                ("user_id", self.ticket_list[i].user_id),
                ("batch_id", str(self.ticket_list[i].batch_id)),
                ("created_at", self.ticket_list[i].created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
        ]) for i in range(4,6)]
        
        expected_response = OrderedDict([
            ("count", len(self.ticket_list)), 
            ("next", None), 
            ("previous", "http://testserver/api/tickets/"), 
            ("results", results)
            ])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)
    
    def test_list_tickets_with_INVALID_permissions(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.commonUser_token}")
        response = self.client.get(self.path)

        expected_response = { "detail": "You do not have permission to perform this action." }

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, expected_response)

