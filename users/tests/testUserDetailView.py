from datetime import datetime
from model_bakery import baker
from collections import OrderedDict
from users.serializers import UserSerializer

from rest_framework.views import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class TestUserDetailView(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:

        cls.commonUser = baker.make("users.User", is_superuser=False)
        cls.superUser = baker.make("users.User", is_superuser=True)

        cls.commonUser_token = Token.objects.create(user=cls.commonUser).key
        cls.superUser_token = Token.objects.create(user=cls.superUser).key

        cls.patch_body = {
            "last_name": "UPDATED last_name"
        }


    @classmethod
    def setUp(cls) -> None:

        cls.ownerUser = baker.make("users.User")
        cls.ownerUser_token = Token.objects.create(user=cls.ownerUser).key

        cls.path = f"/api/users/{cls.ownerUser.id}/"


    def test_get_user_as_owner(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.ownerUser_token}")
        response = self.client.get(self.path)

        expected_response = UserSerializer(self.ownerUser).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_get_user_as_superuser(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.superUser_token}")
        response = self.client.get(self.path)

        expected_response = UserSerializer(self.ownerUser).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_get_user_with_INVALID_permissions(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.commonUser_token}")
        response = self.client.get(self.path)

        expected_response = { "detail": "You do not have permission to perform this action." }

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, expected_response)

    def test_get_WITHOUT_token(self):

        response = self.client.get(self.path)

        expected_response = { "detail": "Authentication credentials were not provided." }

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, expected_response)

    def test_patch_user_as_owner(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.ownerUser_token}")
        response = self.client.patch(self.path, self.patch_body)

        expected_response = {
            **UserSerializer(self.ownerUser).data,
            **self.patch_body
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_patch_user_as_superuser(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.superUser_token}")
        response = self.client.patch(self.path, self.patch_body)

        expected_response = {
            **UserSerializer(self.ownerUser).data,
            **self.patch_body
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_patch_user_with_INVALID_permissions(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.commonUser_token}")
        response = self.client.patch(self.path, self.patch_body)

        expected_response = { "detail": "You do not have permission to perform this action." }

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, expected_response)

    def test_patch_WITHOUT_token(self):

        response = self.client.patch(self.path, self.patch_body)

        expected_response = { "detail": "Authentication credentials were not provided." }

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, expected_response)

    def test_delete_user_as_owner(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.ownerUser_token}")
        response = self.client.delete(self.path)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_user_as_superuser(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.superUser_token}")
        response = self.client.delete(self.path)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_user_with_INVALID_permissions(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.commonUser_token}")
        response = self.client.delete(self.path)

        expected_response = { "detail": "You do not have permission to perform this action." }

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, expected_response)

    def test_delete_WITHOUT_token(self):

        response = self.client.delete(self.path)

        expected_response = { "detail": "Authentication credentials were not provided." }

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, expected_response)

