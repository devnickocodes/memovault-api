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

    def test_create_report_unauthenticated(self):
            self.client.force_authenticate(user=None)
            post_data = {
                'post': self.post.id,
                'reason': 'spam',
                'custom_reason': 'This is a spam report'
            }
            response = self.client.post('/reports/', post_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_report_authenticated_owner(self):
        report = Report.objects.create(post=self.post, reason='spam', owner=self.user)
        update_data = {
            'reason': 'inappropriate',
            'custom_reason': 'This is inappropriate'
        }
        url = f'/reports/{report.id}/'
        response = self.client.patch(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_update_report_authenticated_non_owner(self):
        other_user = User.objects.create_user(username='otheruser', password='12345')
        report = Report.objects.create(post=self.post, reason='spam', owner=other_user)
        update_data = {
            'reason': 'inappropriate',
            'custom_reason': 'This is inappropriate'
        }
        url = f'/reports/{report.id}/'
        response = self.client.patch(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
