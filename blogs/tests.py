from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Blog
from user_management.models import User


class BlogTestCases(APITestCase):

    def setUp(self):
        url = reverse('register')
        data = {
            "username": "gauravpandey",
            "password": "rbvoncvor",
            "email": "aa@gmail.com"
            }
        self.client.post(url, data, format='json')

        url = reverse('login')
        data = {
            "username": "gauravpandey",
            "password": "rbvoncvor",
            "email": "aa@gmai.com"
        }
        resp = self.client.post(url, data, format='json')
        self.auth_token = resp.json()["access"]

        user_obj = User.objects.get(username=data["username"])
        self.user_obj = user_obj
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_create_blogs(self):
        url = reverse('all_blog')
        data = {
            "title": "Sales",
            "content": "This is doc related to sales"
        }
        resp = self.client.post(url, data, format='json', headers={"Authorization": f"Bearer {self.auth_token}"})
        print(resp.json())
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_get_all_blogs(self):
        blog_obj = Blog.objects.create(title="sales",
                            content="Sales content",
                            author=self.user_obj)
        url = reverse('all_blog')
        resp = self.client.get(url, format='json', headers={"Authorization": f"Bearer {self.auth_token}"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.json()[0]["id"], blog_obj.id)

    def test_get_specific_blogs(self):
        blog_obj = Blog.objects.create(title="sales",
                            content="Sales content",
                            author=self.user_obj)
        url = reverse('specific_blog', kwargs={'blog_id': blog_obj.id })
        resp = self.client.get(url, format='json', headers={"Authorization": f"Bearer {self.auth_token}"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.json()["id"], blog_obj.id)

    def test_update_specific_blogs(self):
        blog_obj = Blog.objects.create(title="sales",
                            content="Sales content",
                            author=self.user_obj)
        url = reverse('specific_blog', kwargs={'blog_id': blog_obj.id })
        data = {
            "title": "Sales",
            "content": "This is doc related to sales"
        }
        resp = self.client.put(url, data, format='json', headers={"Authorization": f"Bearer {self.auth_token}"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.json()["title"], data["title"])

    def test_delete_specific_blogs(self):
        blog_obj = Blog.objects.create(title="sales",
                            content="Sales content",
                            author=self.user_obj)
        url = reverse('specific_blog', kwargs={'blog_id': blog_obj.id })
        resp = self.client.delete(url, format='json', headers={"Authorization": f"Bearer {self.auth_token}"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        blog_obj = Blog.objects.filter(id=blog_obj.id)
        self.assertEqual(len(blog_obj), 0)











