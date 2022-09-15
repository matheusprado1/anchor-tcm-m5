from model_bakery import baker

from rest_framework.views import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class TestTicketDeleteView(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:

        cls.ownerUser = baker.make("users.User")
        cls.commonUser = baker.make("users.User", is_superuser=False)
        cls.superUser = baker.make("users.User", is_superuser=True)

        cls.ownerUser_token = Token.objects.create(user=cls.ownerUser).key
        cls.commonUser_token = Token.objects.create(user=cls.commonUser).key
        cls.superUser_token = Token.objects.create(user=cls.superUser).key
        cls.INVALID_token = "10351033"

        cls.INVALID_path = "/api/tickets/f694d31e-5dd2-4b56-aa4b-b3eeb57a0965/"

    @classmethod
    def setUp(cls) -> None:
        
        cls.ticket = baker.make("tickets.Ticket", user=cls.ownerUser)
        cls.path = f"/api/tickets/{cls.ticket.id}/"


    def test_delete_ticket_from_user_as_superUser(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.superUser_token}")
        response = self.client.delete(self.path)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_ticket_from_user_as_owner(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.ownerUser_token}")
        response = self.client.delete(self.path)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_ticket_with_INVALID_permission(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.commonUser_token}")
        response = self.client.delete(self.path)

        expected_response = { "detail": "You do not have permission to perform this action." }

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, expected_response)

    def test_delete_ticket_WITHOUT_token(self):

        response = self.client.delete(self.path)

        expected_response = {
            "detail": "Authentication credentials were not provided."
        }

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, expected_response)

    def test_delete_ticket_with_INVALID_token(self):
        
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.INVALID_token}")
        response = self.client.delete(self.path)

        expected_response = { "detail": "Invalid token." }

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, expected_response)
    

    def test_delete_ticket_for_UNEXISTING_ticket(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.superUser_token}")
        response = self.client.delete(self.INVALID_path)

        expected_response = { "detail": "Not found." }

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, expected_response)
