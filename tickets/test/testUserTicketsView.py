from model_bakery import baker
from collections import OrderedDict

from rest_framework.views import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class TestUserTicketsView(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:

        cls.ownerUser = baker.make("users.User")
        cls.commonUser = baker.make("users.User", is_superuser=False)
        cls.superUser = baker.make("users.User", is_superuser=True)

        cls.ownerUser_token = Token.objects.create(user=cls.ownerUser).key
        cls.commonUser_token = Token.objects.create(user=cls.commonUser).key
        cls.superUser_token = Token.objects.create(user=cls.superUser).key
        cls.INVALID_token = "10351033"

        cls.ticket_list = [baker.make("tickets.Ticket", user_id=cls.ownerUser.id) for i in range(6)]
        # create an aleatory ticket to check if is it filtering correctly
        baker.make("tickets.Ticket")

        cls.path = f"/api/tickets/user/{cls.ownerUser.id}/"
        cls.INVALID_path = "/api/tickets/user/10351033/"

    def test_list_tickets_from_user_as_superUser(self):

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
            ("next", f"http://testserver{self.path}?page=2"), 
            ("previous", None), 
            ("results", results)
        ])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_list_tickets_from_user_as_ownerUser(self):
        
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.ownerUser_token}")
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
            ("next", f"http://testserver{self.path}?page=2"), 
            ("previous", None), 
            ("results", results)
        ])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_paginate_in_list_tickets_from_user(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.superUser_token}")
        response = self.client.get(f"{self.path}?page=2")
        
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
            ("previous", f"http://testserver{self.path}"), 
            ("results", results)
        ])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_list_tickets_from_user_with_INVALID_permission(self):
        
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.commonUser_token}")
        response = self.client.get(self.path)

        expected_response = { "detail": "You do not have permission to perform this action." }

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, expected_response)
    
    def test_list_tickets_from_user_WITHOUT_token(self):

        response = self.client.get(self.path)

        expected_response = { "detail": "Authentication credentials were not provided." }

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, expected_response)

    def test_list_tickets_from_user_with_INVALID_token(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.INVALID_token}")
        response = self.client.get(self.path)

        expected_response = { "detail": "Invalid token." }

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, expected_response)

