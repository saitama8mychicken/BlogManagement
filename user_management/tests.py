from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class BlogTestCases(APITestCase):

    def test_user_registration(self):
        url = reverse('register')
        data = {
            "username": "gauravpandey",
            "password": "rbvoncvor",
            "email": "aa@gmail.com"
            }
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_user_registration_wrong_email(self):
        url = reverse('register')
        data = {
            "username": "gauravpandey",
            "password": "rbvoncvor",
            "email": "aa.com"
        }
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_duplicate_user_registration(self):
        url = reverse('register')
        data = {
            "username": "gauravpandey",
            "password": "rbvoncvor",
            "email": "aa@gmail.com"
        }
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        url = reverse('register')
        data = {
            "username": "gauravpandey",
            "password": "rbvoncvor",
            "email": "aa@gmail.com"
        }
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_generate_access_token(self):
        url = reverse('register')
        data = {
            "username": "gauravpandey",
            "password": "rbvoncvor",
            "email": "aa@gmail.com"
            }
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        url = reverse('login')
        data = {
            "username": "gauravpandey",
            "password": "rbvoncvor",
            "email": "aa@gmail.com"
            }
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_generate_access_token_with_wrong_username(self):
        url = reverse('register')
        data = {
            "username": "gauravpandey",
            "password": "rbvoncvor",
            "email": "aa@gmail.com"
            }
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        url = reverse('login')
        data = {
            "username": "gauravpandey2",
            "password": "rbvoncvor",
            "email": "aa@gmail.com"
            }
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_generate_access_token_with_wrong_password(self):
        url = reverse('register')
        data = {
            "username": "gauravpandey",
            "password": "rbvoncvor",
            "email": "aa@gmail.com"
            }
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        url = reverse('login')
        data = {
            "username": "gauravpandey2",
            "password": "rbvoncvor",
            "email": "aa@gmail.com"
            }
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)






