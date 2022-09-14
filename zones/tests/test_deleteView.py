from email.policy import HTTP

from model_bakery import baker
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status


class ZoneDeleteViewTest(APITestCase):

  @classmethod
  def setUpTestData(cls) -> None:
    cls.ownerUser = baker.make("users.User")
    cls.commonUser = baker.make("users.User", is_superuser=False)
    cls.superUser = baker.make("users.User", is_superuser=True)

    cls.ownerUser_token = Token.objects.create(user=cls.ownerUser).key
    cls.commonUser_token = Token.objects.create(user=cls.commonUser).key
    cls.superUser_token = Token.objects.create(user=cls.superUser).key

    cls.invalid_token = "14258796"
    cls.invalid_path = "/api/zones/34859715"


  @classmethod
  def setUp(cls) -> None:
    cls.zone = baker.make("zones.Zone")
    cls.path = f"/api/zones/{cls.zone.id}/"


  def test_delete_zone_from_user_as_superuser(self):
    self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.superUser_token}")
    response = self.client.delete(self.path)

    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


  def test_delete_zone_from_user_as_owner(self):
    self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.ownerUser_token}")
    response = self.client.delete(self.path)

    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


  def test_delete_zone_without_token(self):
    response = self.client.delete(self.path)

    expected_response = { "detail": "Authentication credentials were not provided."}

    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    self.assertEqual(response.data, expected_response)


  def test_delete_zone_with_invalid_token(self):
    self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.invalid_token}")
    response = self.client.delete(self.path)

    expected_response = { "detail": "Invalid token."}
    
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    self.assertEqual(response.data, expected_response)
