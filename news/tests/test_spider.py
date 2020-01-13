from django.test import TestCase
from news.spider import ycombinator


class SpiderTest(TestCase):
    def setUp(self):
        self.spider = ycombinator()

    def test_defautl_isinstance(self):
        self.assertIsInstance(self.spider, list)

    def test_default_widget_size(self):
        self.assertEqual(len(self.spider), 30)

    def test_default_keys(self):
        self.assertEqual(list(self.spider[0].keys()), ['url', 'title'])
