from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from user.factories import UserFactory

USER_URL = reverse("users")
TOKEN_URL = reverse("user_token")


class TestUser(APITestCase):
    def setUp(self) -> None:
        # UserFactory.create_batch(size=5)
        pass

    def test_user_url(self):
        res = self.client.get(USER_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertNumQueries(1)

    def test_create_user(self):
        payload = {
            "username": "testi",
            "email": "x@example.de",
            "password": "Abc123def",
        }
        res = self.client.post(USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(username=payload["username"])
        self.assertEqual(payload["username"], user.username)

    def test_create_user_invalid_password(self):
        payload = {
            "username": "testi",
            "email": "x@example.de",
            "password": "Abc",
        }
        res = self.client.post(USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = (
            get_user_model().objects.filter(username=payload["username"]).exists()
        )
        self.assertFalse(user_exists)

    def test_username_unique(self):
        UserFactory(username="Bob")
        payload = {
            "username": "Bob",
            "email": "xxx@example.de",
            "password": "Abc123def",
        }
        res = self.client.post(USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_count = (
            get_user_model().objects.filter(username=payload["username"]).count()
        )
        self.assertEqual(user_count, 1)

    def test_create_token(self):
        UserFactory(username="Bob")
        payload = {
            "username": "Bob",
            "password": "abc",
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue("token" in res.data)

    def test_invalid_password_get_token(self):
        UserFactory(username="Bob")
        payload = {
            "username": "Bob",
            "password": "wrong_pass",
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
