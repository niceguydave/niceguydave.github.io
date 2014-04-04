from django.test import TestCase


class PageAccessTest(TestCase):
    """
    Deals with URLs/views which are needed for the proper site functionality
    """

    def test_admin_url_test(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
