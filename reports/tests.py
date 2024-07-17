from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from posts.models import Post
from .models import Report

class ReportTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(title='Test Post', content='This is a test post.', owner=self.user)

    def test_create_report_authenticated(self):
        post_data = {
            'post': self.post.id,
            'reason': 'spam',
            'custom_reason': 'This is a spam report'
        }
        response = self.client.post('/reports/', post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
