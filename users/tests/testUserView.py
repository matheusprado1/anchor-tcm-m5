from uuid import UUID
from datetime import datetime
from model_bakery import baker
from collections import OrderedDict

from rest_framework.views import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class TestTicketView(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:

        cls.commonUser_data = {
            "username": "common_username",
            "email": "common_email@mail.com",
            "cpf": "00000000000",
            "birthdate": "2000-01-01",
            "password": "1234",
            "first_name": "common_first_name",
            "last_name": "common_last_name",
            "is_staff": False,
            "address": {
                "city": "Fortaleza",
                "district": "Siqueira",
                "street": "Rua 01",
                "number": "3",
                "zipcode": "60544-760"
            }
        }

        cls.superUser = baker.make("users.User", is_superuser=True)

        cls.superUser_token = Token.objects.create(user=cls.superUser).key
        cls.INVALID_cpf = "0"
        cls.INVALID_token = "10351033"

        cls.user_list = baker.make("users.User", is_staff=True, _quantity=6)

        cls.path = "/api/users/"


    def test_create_commonUser(self):

        response = self.client.post(self.path, self.commonUser_data, format="json")

        user_data = {** self.commonUser_data}
        user_data.pop("password")

        age = int((
                datetime.now().date() -
                datetime.strptime(self.commonUser_data["birthdate"], '%Y-%m-%d').date()
            ).days/ 365.25)

        expected_response = {
            "id": response.data["id"], 
            **user_data,
            "is_active": True,
            'is_superuser': False,
            "created_at": response.data["created_at"],
            "address": response.data["address"],
            "age": age
        }

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expected_response)


    def test_create_user_with_REPEATED_username(self):

        user_data = {** self.commonUser_data, "username": self.superUser.username}
        response = self.client.post(self.path, user_data, format="json")

        expected_response = { "username": ["This username already exists"] }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)

    def test_create_user_with_REPEATED_email(self):

        user_data = {** self.commonUser_data, "email": self.superUser.email}
        response = self.client.post(self.path, user_data, format="json")

        expected_response = { "email": ["This email address already exists"] }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)

    def test_create_user_with_REPEATED_cpf(self):

        user_data = {** self.commonUser_data, "cpf": self.superUser.cpf}
        response = self.client.post(self.path, user_data, format="json")

        expected_response = { "cpf": ["This cpf number already exists"] }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)

    def test_create_user_with_INVALID_cpf(self):

        user_data = {** self.commonUser_data, "cpf": self.INVALID_cpf}
        response = self.client.post(self.path, user_data, format="json")

        expected_response = { "cpf": ["The cpf field must have 11 digits"] }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)

    def test_create_user_with_EMPTY_address(self):
        user_data = { ** self.commonUser_data }
        user_data["address"] = {}

        response = self.client.post(self.path, user_data, format="json")

        expected_response = {
            "address": { 
                "city": ["This field is required."],
                "district": ["This field is required."],
                "street": ["This field is required."],
                "number": ["This field is required."],
                "zipcode": ["This field is required."]
        }}

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)

    def test_create_user_with_EMPTY_body(self):
        response = self.client.post(self.path, {}, format="json")

        expected_response = {
            "username": ["This field is required."],
            "email": ["This field is required."],
            "cpf": ["This field is required."],
            "birthdate": ["This field is required."],
            "password": ["This field is required."],
            "first_name": ["This field is required."],
            "last_name": ["This field is required."],
            "is_staff": ["This field is required."],
            "address": ["This field is required."]
        }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)


    def test_list_users(self):
        
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.superUser_token}")
        response = self.client.get(self.path)

        complete_user_list = [self.superUser, *self.user_list]

        results = [
            OrderedDict([ 
                ("id", str(complete_user_list[i].id)),
                ("username", complete_user_list[i].username),
                ("is_staff", complete_user_list[i].is_staff),
                ("is_active", complete_user_list[i].is_active),
                ("first_name", complete_user_list[i].first_name),
                ("last_name", complete_user_list[i].last_name),
                ("cpf", complete_user_list[i].cpf),
                ("email", complete_user_list[i].email),
        ]) for i in range(4)]

        expected_response = OrderedDict([
            ("count", len(complete_user_list)), 
            ("next", f"http://testserver{self.path}?page=2"), 
            ("previous", None), 
            ("results", results)
        ])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    
    def test_list_tickets_with_INVALID_token(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.INVALID_token}")
        response = self.client.get(self.path)

        expected_response = { "detail": 'Invalid token.' }

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, expected_response)

