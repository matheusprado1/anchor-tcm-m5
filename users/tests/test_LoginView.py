from datetime import datetime
from model_bakery import baker
from users.models import User
from collections import OrderedDict

from rest_framework.views import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class TestTicketView(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:

        address = baker.make("addresses.Address")
        password = "123456"

        cls.commonUser = User.objects.create_user(**{
            "email": "common_email@mail.com",
            "password": password,
            "username": "common_username",
            "birthdate": "2000-01-01",
            "first_name": "common_first_name",
            "last_name": "common_last_name",
            "is_staff": False,
            "cpf": "00000000000",
            "address": address
        })

        cls.superUser = User.objects.create_superuser(**{
            "email": "super_email@mail.com",
            "password": password,
            "username": "super_username",
            "birthdate": "2000-01-01",
            "first_name": "super_first_name",
            "last_name": "super_last_name",
            "is_staff": False,
            "cpf": "00000000001",
            "address": address
        })


        cls.superUser_token = Token.objects.create(user=cls.superUser).key
        cls.commonUser_token = Token.objects.create(user=cls.commonUser).key

        cls.superUser_login = {
            "email": cls.superUser.email,
            "password": password
        }
        cls.commonUser_login = {
            "email": cls.commonUser.email,
            "password": password
        }


        cls.wrongPassword_login = {
            "email": cls.commonUser.email,
            "password": "secret_password"
        }
        cls.wrongEmail_login = {
            "email": "email@email.com",
            "password": password
        }
        cls.INVALID_email_login = {
            "email": "email@email",
            "password": password
        }

        cls.path = "/api/login/"


    def test_login_commonUser(self):

        response = self.client.post(self.path, self.commonUser_login)
        expected_response = {"token" : self.commonUser_token}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_login_superUser(self):

        response = self.client.post(self.path, self.superUser_login)
        expected_response = {"token" : self.superUser_token}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_login_WRONG_password(self):

        response = self.client.post(self.path, self.wrongPassword_login)
        expected_response = {"detail": "Invalid email or password"}

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)

    def test_login_WRONG_email(self):

        response = self.client.post(self.path, self.wrongEmail_login)
        expected_response = {"detail": "Invalid email or password"}

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)

    def test_login_INVALID_email(self):

        response = self.client.post(self.path, self.INVALID_email_login)
        expected_response = {"email": ["Enter a valid email address."] }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)

    def test_login_with_EMPTY_body(self):
        
        response = self.client.post(self.path, {})
        expected_response = { 
            "email": ["This field is required."],
	        "password": ["This field is required."]
        }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)