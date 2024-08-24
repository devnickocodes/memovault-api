from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from posts.models import Post
from .models import Report


class ReportTests(APITestCase):
    """
    Test suite that covers various scenarios for the `Report` API,
    including creation, retrieval, updating, and deletion of reports.
    It also tests authentication and permissions for different types of users.

    Methods:

        setUp: Sets up the test environment by creating users, a test post,
        and authenticating the client.

        test_create_report_authenticated: Test creating a report when the user
        is authenticated.

        test_create_report_unauthenticated: Test creating a report when the
        user is not authenticated.

        test_update_report_authenticated_owner: Test updating a report by
        the owner of the report.

        test_update_report_authenticated_non_owner: Test updating a report
        by a user who is not the owner.

        test_delete_report_authenticated_owner: Test deleting a report by
        the owner of the report.

        test_delete_report_authenticated_non_owner: Test deleting a report by
        a user who is not the owner.

        test_list_reports_admin_authenticated: Test listing reports with
        admin authentication.

        test_list_reports_admin_unauthenticated: Test listing reports
        without authentication.

        test_retrieve_report_admin_authenticated: Test retrieving a specific
        report with admin authentication.

        test_retrieve_report_admin_unauthenticated: Test retrieving a specific
        report without authentication.
    """
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='12345')
        self.admin = User.objects.create_user(username='admin',
                                              password='123456', is_staff=True)
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(title='Test Post',
                                        content='This is a test post.',
                                        owner=self.user)

    def test_create_report_authenticated(self):
        other_user = User.objects.create_user(username='otheruser',
                                              password='12345')
        other_post = Post.objects.create(title='Another Post',
                                         content='This is another post.',
                                         owner=other_user)

        post_data = {
            'post': other_post.id,
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
        report = Report.objects.create(post=self.post, reason='spam',
                                       owner=self.user)
        update_data = {
            'reason': 'inappropriate',
            'custom_reason': 'This is inappropriate'
        }
        url = f'/reports/{report.id}/'
        response = self.client.patch(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_report_authenticated_non_owner(self):
        other_user = User.objects.create_user(username='otheruser',
                                              password='12345')
        report = Report.objects.create(post=self.post, reason='spam',
                                       owner=other_user)
        update_data = {
            'reason': 'inappropriate',
            'custom_reason': 'This is inappropriate'
        }
        url = f'/reports/{report.id}/'
        response = self.client.patch(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_report_authenticated_owner(self):
        report = Report.objects.create(post=self.post, reason='spam',
                                       owner=self.user)
        url = f'/reports/{report.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_report_authenticated_non_owner(self):
        other_user = User.objects.create_user(username='otheruser',
                                              password='12345')
        report = Report.objects.create(post=self.post, reason='spam',
                                       owner=other_user)
        url = f'/reports/{report.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list_reports_admin_authenticated(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get('/reports/admin/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_reports_admin_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/reports/admin/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_report_admin_authenticated(self):
        report = Report.objects.create(post=self.post, reason='spam',
                                       owner=self.user)
        self.client.force_authenticate(user=self.admin)
        url = f'/reports/admin/{report.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_report_admin_unauthenticated(self):
        self.client.force_authenticate(user=None)
        report = Report.objects.create(post=self.post, reason='spam',
                                       owner=self.user)
        url = f'/reports/admin/{report.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
