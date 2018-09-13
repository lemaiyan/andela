from django.test import TestCase
from app.utils import get_image


class UtilTests(TestCase):

    def setUp(self):
        self.cached = get_image(dimensions='600X600', text='cached')

    def test_get_image(self):
        response = get_image(dimensions='500X500', text='test')
        self.assertEqual(response.status, 200)

    def test_cached_image(self):
        resp = get_image(dimensions='600X600', text='cached')
        self.assertEqual(self.cached.content, resp.content)
