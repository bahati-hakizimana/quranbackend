from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Blog

class BlogTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.blog = Blog.objects.create(title="Test Blog", description="This is a test blog.")

    def test_get_all_blogs(self):
        url = reverse('get_all_blogs')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_blog_by_id(self):
        url = reverse('get_blog_by_id', args=[self.blog.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_blog_by_title(self):
        url = reverse('get_blog_by_title', args=["Test"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_blog(self):
        url = reverse('create_blog')
        data = {'title': 'New Blog', 'description': 'This is a new blog.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_blog(self):
        url = reverse('update_blog', args=[self.blog.id])
        data = {'title': 'Updated Blog', 'description': 'This is an updated blog.'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_blog(self):
        url = reverse('delete_blog', args=[self.blog.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_count_blogs(self):
        url = reverse('count_blogs')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
