import datetime

from django.test import TestCase
from news.models import Post
from news.serializers import NewsSerializer


class NewsSerialiserTest(TestCase):
    def setUp(self):
        self.news_attributes = {
            'title': "Don't just roll the dice – Software pricing guide (2012) [pdf] ",
            'url': "https://neildavidson.com/downloads/dont-just-roll-the-dice-2.0.0.pdf",
            'created': datetime.datetime.now().isoformat()
        }

        self.news = Post.objects.create(**self.news_attributes)
        self.serializer = NewsSerializer(instance=self.news)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'title', 'url', 'created']))