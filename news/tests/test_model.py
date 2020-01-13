from django.test import TestCase

from news.models import Post


class NewsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(
            title="Don't just roll the dice – Software pricing guide (2012) [pdf] ",
            url="https://neildavidson.com/downloads/dont-just-roll-the-dice-2.0.0.pdf"
        )

    def test_title_label(self):
        news = Post(pk=1)
        field_label = news._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Title News')

    def test_name_max_length(self):
        catalog = Post(pk=1)
        max_length = catalog._meta.get_field('title').max_length
        self.assertEquals(max_length, 512)

    def test_url_label(self):
        news = Post(pk=1)
        field_label = news._meta.get_field('url').verbose_name
        self.assertEquals(field_label, 'Url News')

    def test_url_max_length(self):
        news = Post(pk=1)
        max_length = news._meta.get_field('url').max_length
        self.assertEquals(max_length, 200)

